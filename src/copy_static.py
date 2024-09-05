import os
import shutil
from block_markdown import markdown_to_html_node
def copy_files_recursive(source:str , destination:str , cleared=False):
    # return true if exsist
    if not os.path.exists(source)  :
        raise Exception(f'Source:{source} not found.')
    if not os.path.exists(destination):
        raise Exception(f"Destination: {destination} not found.")
    #returns name of paths in directory
    source_list = os.listdir(source)
    if len(source_list) == 0:
        return 0
    if not cleared:
        #removes directory and all content
        shutil.rmtree(destination)
        #makes a new directory at this destination
        os.mkdir(destination)
    result = 1
    for item in source_list:
        # If it is a file copys it to the destination directory
        source_path = os.path.join(source,item)
        if os.path.isfile(source_path):
          new_path =  shutil.copy(source_path, destination)
          result = 0
          print(new_path)
        else:
            destination_path = os.path.join(destination,item)
            os.mkdir(destination_path)
            sub_result = copy_files_recursive(source_path,destination_path,True)
            if sub_result == 0:
                result = 0
    return result


def extract_title(markdown:str)->str:
    lines = markdown.split("\n")
    for line in lines :
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise Exception("No h1 Heading found.")
        
        
def generate_page(from_path , template_path,dest_path):
    try:
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")
        with open(from_path,"r") as f:
            file_contents = f.read()
        with open(template_path,"r") as t:
            template_contents = t.read()
        html_content = markdown_to_html_node(file_contents).to_html()
        title = extract_title(file_contents)
        
        html_page = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
        with open(dest_path,"w") as index:
            index.write(html_page)
        return 0
    except Exception as e:
        print(f"Error while generating page: {e}")
        return 1
        
def generate_pages_recursive(dir_path_content,template_path,dest_dir_path):
    try:
        if not os.path.exists(dir_path_content)  :
            raise Exception(f'Source:{dir_path_content} not found.')
        if not os.path.exists(dest_dir_path):
            raise Exception(f"Destination: {dest_dir_path} not found.")
        if not os.path.exists(template_path):
            raise Exception(f"Template:{template_path} not found")
        list_of_entrys=os.listdir(dir_path_content)
       
        if len(list_of_entrys) == 0:
            return 0
        result = 1
        
        for entry in list_of_entrys:
            current_path = os.path.join(dir_path_content,entry)
            if os.path.isfile(current_path):
                filename = entry
                current_destination = os.path.join(dest_dir_path,filename.replace(".md",".html"))
                generate_page(current_path ,template_path,current_destination)
                result = 0
            else:
                current_destination = os.path.join(dest_dir_path , entry)
                os.mkdir(current_destination)
                sub_result = generate_pages_recursive(current_path , template_path , current_destination)
                if sub_result == 0:
                    result = 0
        return result
    except Exception as e:
        print(f"Error generating page: {e} ")
        return 1
        
        