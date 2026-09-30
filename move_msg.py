import sys

def move_message_section(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the message section
    msg_start = content.find('<!-- Message Section -->')
    if msg_start == -1:
        print(f'Message section not found in {filename}')
        return

    # Find the end of the message section
    msg_end = content.find('    <!-- Leadership Section -->', msg_start)
    if msg_end == -1:
        print(f'End of Message section not found in {filename}')
        return

    msg_html = content[msg_start:msg_end]

    # Remove message section from original position
    content = content[:msg_start] + content[msg_end:]

    # Find where to insert it (after Leadership Section ends, before Organization Section)
    org_start = content.find('    <!-- Organization Structure Section -->')
    if org_start == -1:
        print(f'Organization section not found in {filename}')
        return

    # Insert message section before Organization section
    new_content = content[:org_start] + msg_html + '\n' + content[org_start:]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Successfully updated {filename}')

move_message_section('เกี่ยวกับ UKEM.html')
move_message_section('en/About UKEM.html')
