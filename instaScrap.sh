usernames_file="usernames.txt"
usernames=($(<"$usernames_file"))

# Read curl_template from curl.txt
curl_command=$(<curl.txt)
extracted_username=$(echo "$curl_command" | awk -F'username=' '{print $2}' | sed 's/&.*//')
cleaned_username=$(echo "$extracted_username" | sed "s/' \\\\$//")
echo "Cleaned username: $cleaned_username"

for username in "${usernames[@]}";
do
     curl_with_username=$(echo "$curl_command" | sed "s/$cleaned_username/$username/g")

     # Execute the updated curl command and append the result to instaData.txt
     eval "$curl_with_username" --compressed >> instaData.txt
     python3 instaScrap.py
done