def extract_between(text, start_str, end_str, words_to_remove):

  start_index = text.find(start_str)
  if start_index == -1:
    return ""

  end_index = text.find(end_str, start_index)
  if end_index == -1:
    return ""

  extracted_text = text[start_index + len(start_str):end_index]

  # Remove specified words
  for word in words_to_remove:
    extracted_text = extracted_text.replace(word, '')

  # Header line
  header_line = "point_no,x,y,z\n"
  cleaned_text = header_line + extracted_text

  # Remove empty lines
  cleaned_text = "\n".join([line for line in cleaned_text.splitlines() if line])

  return cleaned_text

with open("points_only.anf", "r") as f:
  text = f.read()

# Word to remove
words_to_remove = ["NULL_ID", "kpt,"] 

xyz_points = extract_between(text, "else", "*endif", words_to_remove)

# Write to file
with open("xyz_points.txt", "w") as output_file:
  output_file.write(xyz_points)

print('Complete')