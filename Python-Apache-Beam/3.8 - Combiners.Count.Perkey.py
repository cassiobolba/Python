import apache_beam as beam

p1 = beam.Pipeline()

Qtd_Atrasos = (
    p1
    | "Importar Dados" >> beam.io.ReadFromText("voos_sample.csv", skip_header_lines = 1)
    | "Separar por Vírgulas" >> beam.Map(lambda record: record.split(','))
    | "Pegar voos de Los Angeles" >> beam.Filter(lambda record: int(record[8]) > 0 )
    | "Criar par" >> beam.Map(lambda record: (record[4],int(record[8])))
    | "Contar por key" >> beam.combiners.Count.PerKey()
    | "Mostrar Resultados" >> beam.Map(print)
)

p1.run()