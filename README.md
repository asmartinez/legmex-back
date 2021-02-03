# colegio-elasticsearch

## Paguina para buscar en la coleccion de documentos

/v1/search/

Peticion GET

/v1/search/?search=engine&fields=dispositionTitle,date,volume,legislationTranscriptCopy

"search":"<palabra_a_buscar>",

"fields":"dispositionTitle,date,volume" 

Si no se envia fields en la peticion GET se hace una busqueda en todos los campos, se tiene que separar con coma ( , ) cada campo especifico en donde deseas buscar 

Devuelve una clave http 202 OK

Ya tiene archivos subidos se puede hacer una busqueda "engine" para que te devuelva todos los datos

devuelve un json con cada documento y con la misma forma con la que se suben los documentos

{
        "dispositionTitle",
        "date",
        "volume",
        "pageNumbers",
        "legislationTranscriptCopy",
        "place",
        "dispositionNumber",
        "dispositionTypeId",
        "affairId",
}

## Paguina para subir documentos

/v1/upload/

Peticion POST

Se sube con un formulario html con los siguientes campos

{
        "dispositionTitle",
        "date",
        "volume",
        "pageNumbers",
        "legislationTranscriptOriginal",
        "legislationTranscriptCopy",
        "place",
        "dispositionNumber",
        "dispositionTypeId",
        "affairId",
}

Devuelve el mismo documento que se creo con una respuesta http 202 OK