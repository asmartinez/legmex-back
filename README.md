# colegio-elasticsearch

## Paguina para buscar en la coleccion de documentos

/v1/buscar/

Peticion GET

json con forma 

{
  "search":"<Termino_a_buscar>"
}

Devuelve una clave http 302 FOUND

Ya tiene archivos subidos se puede hacer una busqueda "engine" para que te devuelva todos los datos

devuelve un json con cada documento y con la misma forma con la que se suben los documentos

{
        "nombre":"<Nombre_texto>",
        "autor":"<Autor_texto>",
        "texto":"<Texto>"
}

## Paguina para subir documentos

/v1/subir/

Peticion POST

Se sube con un formulario html

{
        "nombre":"<Nombre_texto>",
        "autor":"<Autor_texto>",
        "texto":"<Texto> <Este texto puede ser tan largo como se ocupe, parecido a un textarea>"
        "archivo":"<archivo del documento><formato pdf>"
}

Devuelve el mismo documento que se creo con una respuesta http 201 created