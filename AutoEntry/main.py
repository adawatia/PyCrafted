import pandas as  pd

def automate_entry(data,file_path):
    try:
        
        try:
            existing_data = pd.read_csv(file_path)
        except FileNotFoundError:
            existing_data = pd.DataFrame()
            
        new_data = pd.DataFrame(data)
        combined_data = pd.concat([existing_data,new_data],ignore_index=True)
        combined_data.to_csv(file_path,index=False)
        print("Data Entry Successfull!")
    except Exception as e:
        print(f"An error ocurred: {e}")
        

