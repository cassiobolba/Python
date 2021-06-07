import apache_beam as beam

# definir pipeline
p1 = beam.Pipeline()

voos = (
p1
  # ler arquivo, e excluir o cabeçalho
  # as pipes significam que um comando é usado como input do outro
  | "Importar Dados" >> beam.io.ReadFromText("voos_sample.csv", skip_header_lines = 1)
  | "Separar por Vírgulas" >> beam.Map(lambda record: record.split(','))
  | "Mostrar Resultados" >> beam.Map(print)
)

# comando para executar
p1.run()
