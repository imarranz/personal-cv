 
#file_input_ = open('041_Publications.md','r')
#file_output_ = open('041_Publications_last_five_years.md', 'w')

#for line_ in file_input_:
    
    #if '### 2018' in line_:
        #break
    #else:
        #file_output_.write(line_)
        
#file_input_.close()
#file_output_.close()
    
#file_input_ = open('071_Congress.md','r')
#file_output_ = open('071_Congress_last_five_years.md', 'w')

#for line_ in file_input_:
    
    #if '### 2016' in line_:
        #break
    #else:
        #file_output_.write(line_)
        
#file_input_.close()
#file_output_.close()

def filter_publications(input_file, output_file, cutoff_year):
    """
    Filters content from the input file up to the specified year and writes it to the output file.

    Parameters
    ----------
    input_file : str
        The path to the input markdown file containing the publications or congress entries.
    output_file : str
        The path where the filtered markdown file will be saved.
    cutoff_year : str
        The year up to which the entries are to be included in the output file. This is a string representing the year (e.g., '2018').

    Returns
    -------
    None

    Examples
    --------
    >>> filter_publications('041_Publications.md', '041_Publications_last_five_years.md', '2018')

    >>> filter_publications('071_Congress.md', '071_Congress_last_five_years.md', '2016')
    """

    # Construct the cutoff marker using the provided year
    cutoff_marker = f"### {cutoff_year}"

    # Open the input file for reading
    with open(input_file, 'r') as file_input:
        # Open the output file for writing
        with open(output_file, 'w') as file_output:
            # Read each line from the input file
            for line in file_input:
                # Check if the line contains the cutoff year marker
                if cutoff_marker in line:
                    break
                else:
                    # Write the line to the output file
                    file_output.write(line)

    # Files are automatically closed when exiting the 'with' blocks

# Example usage of the function
if __name__ == "__main__":
    filter_publications('041_Publications.md', '041_Publications_last_five_years.md', '2018')
    filter_publications('071_Congress.md', '071_Congress_last_five_years.md', '2018')
