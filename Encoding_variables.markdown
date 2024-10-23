### what should you encoding data ? 

we should encoding categroical data like {'cat' , 'Dog' } , to make the model can relate with data . 

----
### what is types of Discrete L Categorical Data ? 

#### Ordinal : الترتيب فيها مهم 
possible classes like : {'small' , 'medium' , 'large'}

##### ordinal Category variable Encoding : 
\- use mapping  , for example : 
'small' -> 0 
'medium' -> 1 
'large' -> 2 , and so on ... 

in code : 

```python
size_mapping = {'small': 1, 'medium': 2, 'large': 3}
# Apply the mapping to the 'Size' column
df['Size_encoded'] = df['Size'].map(size_mapping)
```

-----

 #### Nominal : الترتيب فيها مش مهم  
Possible classes like : {'cat' , 'Dog' }

##### Nominal Category variable Encoding : 
\- using 'One-hot' Encoding : 
![alt text](image.png) 

----

\- using 'Dummy' Encoding : 
the same 'one-hot' encoding but , with some different in mathamtical . 
الفرق انه بيفرض التصنيف التالت بإنه يقول لو مش التصنيف الاول ولا التاني يبقي التالت و بكده انا مش محتاج اعمل جدول للتصنيف التالت لذلك سمي بال 
dummy encoding 
![alt text](image-1.png)