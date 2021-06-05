Este codigo al ser ejecutado, solicita la ruta de un CSV que se encuentre separado por ";".
Al agregar un DF con los siguientes campos:

fiscal_id, first_name,last_name,gender,fecha_nacimiento,fecha_vencimiento,deuda,direccion,correo,estatus_contacto,prioridad,telefono

El codigo creara tres distintos DF, uno donde se mostrara la informacion personal del cliente, el segundo el correo de contacto de los clientes y por ultimo los datos de contacto telefonico de los clientes.

Estos dataframes se almacenaran en formato ".xlsx" en el repositorio de output para poder tener un fácil acceso a ellos. A su vez, se guardaran dentro de un database que podra ser accedido por SQLite.

Para finalizar, en el repositorio se encuentra un archivo "txt" con los requerimientos para ejecutar el codigo utilizando Python 3.8.