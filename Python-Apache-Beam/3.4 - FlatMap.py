import apache_beam as beam

p1 = beam.Pipeline()

Collection = (
    p1
    |beam.io.ReadFromText('poema.txt')
    |beam.FlatMap(lambda record: record.split(' '))
    |beam.io.WriteToText('resultado.txt')
)
p1.run()