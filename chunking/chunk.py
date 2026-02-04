from __future__ import annotations

import argparse
import json
from pathlib import Path

from docling.document_converter import DocumentConverter


def chunk_text(text: str, chunk_size: int = 2500, overlap: int = 500) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if overlap < 0:
        raise ValueError("overlap must be >= 0")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    step = chunk_size - overlap
    chunks: list[str] = []
    for start in range(0, len(text), step):
        chunk = text[start : start + chunk_size]
        if chunk:
            chunks.append(chunk)
    return chunks


def convert_pdfs_to_markdown(
    input_dir: Path,
    markdown_dir: Path,
    output_jsonl: Path,
    chunk_size: int,
    overlap: int,
    glob_pattern: str,
) -> None:
    pdfs = sorted(input_dir.rglob(glob_pattern))
    if not pdfs:
        print(f"No PDFs found under {input_dir} with pattern '{glob_pattern}'.")
        return

    markdown_dir.mkdir(parents=True, exist_ok=True)
    output_jsonl.parent.mkdir(parents=True, exist_ok=True)

    converter = DocumentConverter()

    total_chunks = 0
    with output_jsonl.open("w", encoding="utf-8") as out:
        for pdf_path in pdfs:
            result = converter.convert(str(pdf_path))
            markdown = result.document.export_to_markdown()

            md_path = markdown_dir / f"{pdf_path.stem}.md"
            md_path.write_text(markdown, encoding="utf-8")

            chunks = chunk_text(markdown, chunk_size=chunk_size, overlap=overlap)
            for idx, chunk in enumerate(chunks, start=1):
                record = {
                    "pdf_name": pdf_path.name,
                    "chunk_teaxt": chunk,
                    "chunk_no": idx,
                }
                out.write(json.dumps(record, ensure_ascii=True) + "\n")

            total_chunks += len(chunks)
            print(
                f"Converted {pdf_path.name} -> {md_path.name} "
                f"({len(chunks)} chunks)"
            )

    print(f"Done. Wrote {total_chunks} chunks to {output_jsonl}.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert PDFs to Markdown, then chunk into JSONL."
    )
    parser.add_argument(
        "--input-dir",
        default="doc/splits",
        help="Directory containing PDFs",
    )
    parser.add_argument(
        "--markdown-dir",
        default="doc/markdown",
        help="Directory to write Markdown files",
    )
    parser.add_argument(
        "--output-jsonl",
        default="doc/chunks.jsonl",
        help="Path to output JSONL file",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=2500,
        help="Chunk size in characters",
    )
    parser.add_argument(
        "--chunk-overlap",
        type=int,
        default=500,
        help="Chunk overlap in characters",
    )
    parser.add_argument(
        "--glob",
        default="*.pdf",
        help="Glob pattern for PDFs under input-dir",
    )
    args = parser.parse_args()

    convert_pdfs_to_markdown(
        input_dir=Path(args.input_dir),
        markdown_dir=Path(args.markdown_dir),
        output_jsonl=Path(args.output_jsonl),
        chunk_size=args.chunk_size,
        overlap=args.chunk_overlap,
        glob_pattern=args.glob,
    )


if __name__ == "__main__":
    main()
