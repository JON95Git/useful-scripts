
print("Python pointers")
data_number_id = "12345"
data_letter_id = "abcde"

data_dict = {
   "number": {
        "id": {data_number_id},
        "counter": 1
    },

  "letter": {
        "id": {data_letter_id},
        "counter": 1
    },
}

id = data_number_id

if (id == data_number_id):
    print("number")
    data_entry = data_dict["number"]
else:
    print("letter")
    data_entry = data_dict["letter"]

print(data_entry)
