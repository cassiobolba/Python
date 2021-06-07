import apache_beam as beam

p = beam.Pipeline()

negros = ('Adão','Jesus','Mike')
brancos = ('Tulio','Mary','Joca')
indios = ('Vic','Marta','Tom')

negros_pc = p | "Criando Pcollection negros" >> beam.Create(negros)
brancos_pc = p | "Criando Pcollection brancos" >> beam.Create(brancos)
indios_pc = p | "Criando Pcollection indios" >> beam.Create(indios)

pessoas = ((negros_pc,brancos_pc,indios_pc) | beam.Flatten()) | beam.Map(print)
p.run()