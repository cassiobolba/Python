import apache_beam as beam

p1 = beam.Pipeline()

voos = (
p1
  | "Importar Dados" >> beam.io.ReadFromText("voos_sample.csv", skip_header_lines = 1)
  | "Separar por Vírgulas" >> beam.Map(lambda record: record.split(','))
  | "Pegar voos de Los Angeles" >> beam.Filter(lambda record: record[3] == "LAX")
  | "Mostrar Resultados" >> beam.Map(print)
)

p1.run()