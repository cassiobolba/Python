import apache_beam as beam

p1 = beam.Pipeline()

p1 | "Tupla" >> beam.Create( [ ("Cassio",32) , ("Vics",21) ] ) | "print Tupla" >> beam.Map(print) #tupla
p1 | "Lista" >> beam.Create ( [ 1,2,3 ] ) |  "print Lista" >> beam.Map(print) #lista

p1.run()