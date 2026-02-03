
import PyPDF2
import re
import string
from pathlib import Path


FILE_NAME = [
"RP 101 Wind Turbine Gear Lubricant Flushing Procedures",
"RP 102 Wind Turbine Gearbox Oil Sampling Procedure",
"RP 105 Factors Indicating Gear Lube Oil Change",
"RP 106 Wind Turbine Gear Oil Filtration Procedure",
"RP 201 Generator Collector Ring Assembly Maintenance",
"RP 202 Grease Lubricated Bearing Maintenance",
"RP 203 Generator Off-Line Electrical Testing",
"RP 204 Converter Maintenance",
"RP 207 Wind Turbine Generator and Converter Types",
"RP 208 Shaft Current Management",
"RP 301 Wind Turbine Blades",
"RP 302 Rotor Hubs",
"RP 304 Rotor Lightning Protection Systems",
"RP 401 Foundation Inspections, Maintenance, Base Bolt Tensioning",
"RP 402 Fall Protection, Rescue Systems, Climb Assist and Harness",
"RP 404 Wind Turbine Elevators",
"RP 502 Smart Grid Data Reporting",
"RP 503 Wind Turbine Reliability",
"RP 504 Wind Forecasting Data",
"RP 505 Asset Identification and Data Reporting",
"RP 506 Wind Turbine Key Performance Indicators",
"RP 507 Wind Turbine Condition Based Maintenance",
"RP 508 Oil Analysis Data Collection and Reporting Procedures",
"RP 509 GADS Reporting Practices",
"RP 510 Substation Data Collection",
"RP 601 Wind Energy Power Plant Collector System Maintenance",
"RP 602 Wind Energy Power Plant Substation and Transmission Line Maintenance",
"RP 701 Wind Project End of Warranty Management and Inspections",
"RP 801 Condition Based Maintenance",
"RP 811 Vibration Analysis for Wind Turbines",
"RP 812 Wind Turbine Main Bearing Grease Sampling Procedures",
"RP 813 Wind Turbine Generator Bearing Grease Sampling Procedures",
"RP 814 Wind Turbine Pitch Bearing Grease Sampling Procedures",
"RP 815 Wind Turbine Grease Analysis Test Methods",
"RP 816 Wind Turbine Temperature Measurement Procedures",
"RP 817 Wind Turbine Nacelle Process Parameter Monitoring",
"RP 818 Wind Turbine On-line Gearbox Debris Condition Monitoring",
"RP 819 Online Oil Condition Monitoring",
"RP 821 Wing Turbine Blade Condition Monitoring",
"RP 831 Condition Monitoring of Electrical and Electronic Components of Wind Turbines",
"RP 832 Lighting Protection System Condition Based Monitoring",
"RP 901 Quality During Wind Project Construction",
"RP 902 Lean In an Operational Environment"
]



STOP_WORDS = [
"RP 101 Wind Turbine Gear Lubricant Flushing Procedures",
"RP 102 Wind Turbine Gearbox Oil Sampling Procedure",
"RP 105 Factors Indicating Gear Lube Oil Change",
"RP 106 Wind Turbine Gear Oil Filtration Procedure",
"RP 201 Generator Collector Ring Assembly Maintenance",
"RP 202 Grease Lubricated Bearing Maintenance",
"RP 203 ",
"RP 204 Converter Maintenance",
"RP 207 Wind Turbine Generator and Converter Types",
"RP 208 Shaft Current Management",
"RP 301 Wind Turbine Blades",
"RP 302 Rotor Hubs",
"RP 304 Rotor Lightning Protection Systems",
"RP 401 Foundation Inspections, Maintenance, and Base Bolt Tensioning Procedures",
"RP 402 Fall Protection, Rescue Systems",
"RP 404 Wind Turbine Elevators",
"RP 502 Smart Grid Data Reporting",
"RP 503 Wind Turbine Reliability",
"RP 504 Wind Forecasting Data",
"RP 505 Asset Identification and Data Reporting",
"RP 506 Wind Turbine Key Performance Indicator",
"RP 507 Wind Turbine Condition Based Maintenance",
"RP 508 Oil Analysis Data Collection and Reporting Procedures",
"RP 509 NERC GADS Reporting Practices",
"RP 510 HV Substation Data Collection",
"RP 601 Wind Energy Power Plant Collector System Maintenance",
"RP 602 Wind Energy Power Plant Substation and Transmission Line Maintenance",
"RP 701 Wind Project End of Warranty Management and Inspections",
"RP 801 Condition Based Maintenance",
"RP 811 Vibration Analysis for Wind Turbines",
"RP 812 Wind Turbine Main Bearing Grease Sampling Procedures",
"RP 813 Wind Turbine Generator Bearing Grease Sampling Procedures",
"RP 814 Wind Turbine Pitch Bearing Grease Sampling Procedures",
"RP 815 Wind Turbine Grease Analysis Test Methods",
"RP 816 Wind Turbine Temperature Measurement Procedures",
"RP 817 Wind Turbine Nacelle Process Parameter Monitoring",
"RP 818 Wind Turbine On",
"RP 819 Online Oil Condition Monitoring",
"RP 821 Wind Turbine Blade Condition Monitoring",
"RP 831 Condition Monitoring of Electrical and Electronic Components of Wind Turbines",
"RP 832 Lightning Protection System Condition",
"RP 901 Quality During Wind Project Construction",
"RP 902 Lean In an Operational Environment"
]


pdf_path = 'doc/manual.pdf'


def normalize_text(text: str) -> str:
    """
    Normalize text by removing punctuation, extra whitespace, line breaks, and converting to lowercase.
    
    Args:
        text: Input text to normalize
    
    Returns:
        Normalized text with single spaces, no punctuation, and lowercase
    """
    # Convert to lowercase
    text = text.lower()
    # Remove all punctuation marks
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Replace all whitespace (spaces, tabs, newlines) with single space
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespace
    text = text.strip()
    return text


def find_string_pages(pdf_path: str, search_strings: list[str], start_page: int = 8) -> dict[str, list[int]]:
    """
    Find page numbers where each search string appears in the PDF.
    
    Args:
        pdf_path: Path to the PDF file
        search_strings: List of strings to search for
        start_page: Page number to start searching from (1-indexed)
    
    Returns:
        Dictionary mapping each string to list of page numbers where it appears
    """
    results = {string: [] for string in search_strings}
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)
        
        # Convert to 0-indexed for internal processing
        start_idx = start_page - 1
        
        print(f"Searching {total_pages} pages (starting from page {start_page})...")
        print("-" * 80)
        
        for page_num in range(start_idx, total_pages):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            # Normalize page text (lowercase, single spaces, no line breaks)
            normalized_page_text = normalize_text(page_text)
            
            # Search for each string in the current page (case and whitespace insensitive)
            for search_string in search_strings:
                normalized_search = normalize_text(search_string)
                if normalized_search in normalized_page_text:
                    # Store 1-indexed page number
                    results[search_string].append(page_num + 1)
        
    return results


def print_search_results(results: dict[str, list[int]]) -> None:
    """Print the search results in a readable format."""
    found_count = sum(1 for pages in results.values() if pages)
    total_count = len(results)
    
    print(f"\nSearch complete! Found {found_count}/{total_count} strings")
    print("=" * 80)
    
    for search_string, page_numbers in results.items():
        if page_numbers:
            pages_str = ", ".join(map(str, page_numbers))
            print(f"\n✓ '{search_string}'")
            print(f"  Found on page(s): {pages_str}")
        else:
            print(f"\n✗ '{search_string}'")
            print(f"  Not found")


def get_first_occurrence_pages(results: dict[str, list[int]]) -> list[tuple[str, int]]:
    """
    Get the first occurrence page for each stop word.
    
    Args:
        results: Dictionary mapping stop words to list of page numbers
    
    Returns:
        List of tuples (stop_word, first_page_number) sorted by page number
    """
    first_occurrences = []
    
    for stop_word, pages in results.items():
        if pages:
            first_page = min(pages)
            first_occurrences.append((stop_word, first_page))
    
    # Sort by page number
    first_occurrences.sort(key=lambda x: x[1])
    
    return first_occurrences


def split_pdf_by_stop_words(
    pdf_path: str,
    stop_words: list[str],
    file_names: list[str],
    output_dir: str = 'doc/splits',
    start_page: int = 10
) -> None:
    """
    Split PDF into smaller PDFs based on stop word occurrences.
    
    Logic:
    - Start page: first occurrence of a stop word
    - End page: one page before the next stop word occurrence
    - File name: corresponding name from FILE_NAME list at same index
    
    Args:
        pdf_path: Path to input PDF
        stop_words: List of stop words to search for
        file_names: List of file names corresponding to each stop word
        output_dir: Directory to save split PDFs
        start_page: Page number to start searching from (1-indexed)
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all occurrences of stop words
    print("Finding stop words in PDF...")
    results = find_string_pages(pdf_path, stop_words, start_page)
    
    # Get first occurrence of each stop word
    first_occurrences = get_first_occurrence_pages(results)
    
    if not first_occurrences:
        print("No stop words found in PDF!")
        return
    
    print(f"\nFound {len(first_occurrences)} sections to split")
    print("=" * 80)
    
    # Open the input PDF
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)
        
        # Process each section
        for i, (stop_word, start_page_num) in enumerate(first_occurrences):
            # Find the index of this stop word in the original STOP_WORDS list
            try:
                stop_word_index = stop_words.index(stop_word)
                output_filename = file_names[stop_word_index]
            except (ValueError, IndexError):
                print(f"Warning: Could not find matching file name for '{stop_word}'")
                output_filename = f"section_{i+1}"
            
            # Determine end page (one page before next stop word, or end of PDF)
            if i + 1 < len(first_occurrences):
                end_page_num = first_occurrences[i + 1][1] - 1
            else:
                end_page_num = total_pages
            
            # Create a new PDF writer for this section
            pdf_writer = PyPDF2.PdfWriter()
            
            # Add pages from start to end (convert to 0-indexed)
            for page_num in range(start_page_num - 1, end_page_num):
                if 0 <= page_num < total_pages:
                    pdf_writer.add_page(pdf_reader.pages[page_num])
            
            # Save the split PDF
            output_file = output_path / f"{output_filename}.pdf"
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)
            
            page_count = end_page_num - start_page_num + 1
            print(f"\n✓ Created: {output_filename}.pdf")
            print(f"  Pages: {start_page_num}-{end_page_num} ({page_count} pages)")
            print(f"  Stop word: '{stop_word}'")
    
    print("\n" + "=" * 80)
    print(f"Split complete! Created {len(first_occurrences)} PDF files in '{output_dir}/'")


def create_split_report(
    pdf_path: str,
    stop_words: list[str],
    file_names: list[str],
    start_page: int = 10
) -> None:
    """
    Create a report showing how the PDF would be split without actually splitting it.
    
    Args:
        pdf_path: Path to input PDF
        stop_words: List of stop words to search for
        file_names: List of file names corresponding to each stop word
        start_page: Page number to start searching from (1-indexed)
    """
    # Find all occurrences of stop words
    results = find_string_pages(pdf_path, stop_words, start_page)
    
    # Get first occurrence of each stop word
    first_occurrences = get_first_occurrence_pages(results)
    
    if not first_occurrences:
        print("No stop words found in PDF!")
        return
    
    print(f"\nPDF Split Report")
    print("=" * 80)
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)
        
        for i, (stop_word, start_page_num) in enumerate(first_occurrences):
            # Find the index and corresponding file name
            try:
                stop_word_index = stop_words.index(stop_word)
                output_filename = file_names[stop_word_index]
            except (ValueError, IndexError):
                output_filename = f"section_{i+1}"
            
            # Determine end page
            if i + 1 < len(first_occurrences):
                end_page_num = first_occurrences[i + 1][1] - 1
            else:
                end_page_num = total_pages
            
            page_count = end_page_num - start_page_num + 1
            
            print(f"\nSection {i+1}:")
            print(f"  File name: {output_filename}.pdf")
            print(f"  Pages: {start_page_num}-{end_page_num} ({page_count} pages)")
            print(f"  Stop word: '{stop_word}'")




if __name__ == "__main__":
    # Option 1: Create a report showing how the PDF would be split (preview)
    # create_split_report(pdf_path, STOP_WORDS, FILE_NAME, start_page=10)
    
    # Option 2: Actually split the PDF into smaller files
    split_pdf_by_stop_words(
        pdf_path=pdf_path,
        stop_words=STOP_WORDS,
        file_names=FILE_NAME,
        output_dir='doc/splits',
        start_page=10
    )


