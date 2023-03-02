import pandas as pd
from sqlalchemy import create_engine

print ("Ingrese path del csv") 
file_name = input()
df= pd.read_csv(file_name,sep=";")
df= df.drop(["altura","peso"], axis=1)

df[["fecha_nacimiento","fecha_vencimiento"]] = df[["fecha_nacimiento","fecha_vencimiento"]].apply(pd.to_datetime, format='%Y-%m-%d')

now = pd.to_datetime('now')
df['edad'] = (now.year - df['fecha_nacimiento'].dt.year) - ((now.month - df['fecha_nacimiento'].dt.month) < 0)
df['delinquency'] = (now.day - df['fecha_vencimiento'].dt.day)

labels = ['1', '2', '3', '4', '5', '6']
bins = [20,21,31,41,51,61,100]
df['age_group'] = pd.cut(df.edad, bins, labels = labels,right=False)

clientes = pd.DataFrame()
clientes[["fiscal_id","first_name","last_name","gender","birth_date","age","age_group","due_date","delinquency","due_balance","address"]]= \
  df[["fiscal_id","first_name","last_name","gender","fecha_nacimiento","edad","age_group","fecha_vencimiento","delinquency","deuda","direccion"]]
clientes[["fiscal_id", "first_name","last_name","gender","address"]] = \
  clientes[["fiscal_id", "first_name","last_name","gender","address"]].apply(lambda x: x.astype(str).str.upper())
clientes["age_group"] = clientes["age_group"].astype("int64")
writer = pd.ExcelWriter('output/clientes.xlsx',datetime_format='dd mm yyyy')
print(clientes.head())
df.to_excel(writer)
writer.save()
engine = create_engine('sqlite:///database.db3')
clientes.to_sql("clientes",con=engine)

emails = pd.DataFrame()
emails [["fiscal_id","email","status","priority"]] = df[["fiscal_id","correo","estatus_contacto","prioridad"]]
emails [["fiscal_id","email","status"]] = df[["fiscal_id","correo","estatus_contacto"]].apply(lambda x: x.astype(str).str.upper())
emails ["priority"] = df["prioridad"].fillna(0).astype("int64")
writer = pd.ExcelWriter('output/emails.xlsx', engine='xlsxwriter')
df.to_excel(writer)
writer.save()
emails.to_sql("emails",con=engine)


phones = pd.DataFrame()
phones [["fiscal_id","phone","status","priority"]] = df[["fiscal_id","telefono","estatus_contacto","prioridad"]]
phones [["fiscal_id","status"]] = df[["fiscal_id","estatus_contacto"]].apply(lambda x: x.astype(str).str.upper())
phones ["phone"] = df["telefono"].fillna(0).astype("int64").astype("string")
phones ["priority"] = df["prioridad"].fillna(0).astype("int64")
writer = pd.ExcelWriter('output/phones.xlsx', engine='xlsxwriter')
df.to_excel(writer)
writer.save()
phones.to_sql("phones",con=engine)

#Cambios para luis y su nueva rama
