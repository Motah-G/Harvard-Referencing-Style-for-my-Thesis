def generate_harvard_reference():
    # first data entry
    authors = input(" write the name of Author(s) (Last name, First name; separate multiple authors with commas): ")
    year = input("Year of publication: ")
    title = input("Title of the work: ")
    publication = input("Publication: ")
    page = input("page: ")
    url = input("URL (optional): ")

    # The author names
    # authors_list = [author.strip() for author in authors.split(",")]
    # formatted_authors = []
    # for author in authors_list:
    #     author_parts = author.split(" ")
    #     last_name = author_parts[-1].strip(",")
    #     first_name = " ".join(author_parts[:-1])
    #     formatted_name = f"{last_name}, {first_name}"
    #     formatted_authors.append(formatted_name)

    # Create the Harvard reference
    # reference = ", ".join(formatted_authors)
    reference = f"  {authors}.  ({year}). {title}. {publication}. Pp{page}."
    if url:
        reference += f" Available at: {url}."
    # 
    
    return reference


# Generate Harvard reference
harvard_reference = generate_harvard_reference()

# Print the generated reference
print("Harvard Reference:")
print(harvard_reference)
