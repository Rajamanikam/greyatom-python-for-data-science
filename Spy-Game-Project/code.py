# --------------
#Part - 1

def read_file(path):
    file = open(path, "r")
    sentence = file.read()
    file.close()
    return sentence

sample_message = read_file(file_path)
print(str(sample_message)) 

#Part - 2
message1 = read_file(file_path_1)
message2 = read_file(file_path_2)
print(message1)
print(message2)

#Part - 3
def fuse_msg(message_a, message_b):
    quotient = int(message_b) // int(message_a)
    return quotient

secret_msg_1 = fuse_msg(message1, message2)
secret_msg_1 = str(secret_msg_1)
print(secret_msg_1)

#Part - 4
message_3 = read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
    sub = ""
    if message_c == "Red":
        sub = "Army General"
    elif message_c == "Green":
        sub = "Data Scientist"
    elif message_c == "Blue":
        sub = "Marine Biologist"
    return sub

secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)

#Part - 5
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)

def compare_msg(message_d, message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [item for item in a_list if item not in b_list]
    final_msg = " ".join(c_list)
    return final_msg

secret_msg_3 = compare_msg(message_4, message_5)
print(secret_msg_3)

#Part - 6
message_6 = read_file(file_path_6)
print(message_6)

def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x : len(x) % 2 == 0
    b_list = list(filter(even_word, a_list))
    final_msg = " ".join(b_list)
    return final_msg
    
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)

#Part - 7
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg = " ".join(message_parts)
final_path= user_data_dir + '/secret_message.txt'

def write_file(secret_msg, path):
    f = open(path, 'a+')
    f.write(secret_msg)
    f.close()

write_file(secret_msg,final_path)

print(secret_msg)










