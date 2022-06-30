<py-script>
  from js import console
  import pandas as pd 
  import re
  from pyodide.http import open_url
  import array

  def my_function(*args, **kwargs):


      url_content = open_url("https://raw.githubusercontent.com/Swal27/ekstraksi/main/Fixjaktim.csv")
      
      text = Element('test-input').element.value

      #print('text:', text)
      console.log(f'text: {text}')

      df=pd.read_csv(url_content) 
      data = df.loc[:,['date','from','to','condition']] 
      #my_list = ['jaktim', 'jakarta timur', 'Jaktim', 'Jakarta Timur'] 
      #ndata = data[data['Content'].str.contains("|".join(my_list), regex=True, flags=re.IGNORECASE)].reset_index(drop=True)
      arr = []
      arr.append(text)
      ndataf = data[data['from'].str.contains("|".join(arr), regex=True, flags=re.IGNORECASE)].reset_index(drop=True)
      Element('output').element.innerText = ndataf['date'].to_string(index=False)
  </py-script>