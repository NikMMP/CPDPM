import numpy
import matplotlib
import sys 
import math

class Truck:
   def __init__(self, data):

     m = data["mass"]
     jd = data["jd"]
     c1 = data["c1"]
     c2 = data["c2"]
     b = data["b"]
     l = data["l"]

     self.bs1 = data["bs"]
     self.as1 = data["as"]

     a1 = data["a1"]
     a2 = data["a2"]
     v = data["v"]

     self.M = numpy.array([ [m ,0.0], [0.0, jd] ])
     self.K = numpy.array([ [ c1 + c2, c1 * b - c2 * (l-b)], [c1 * b - c2 * (l-b), c1 * pow(b,2) + c2 * pow(l-b,2)]]) 
     self.C = numpy.array([ [ a1 + a2, a1 * b - a2 * (l - b)], [ a1 * b - a2 * (l - b), a1 * pow(b,2) + a2 * pow(l-b,2)]])
     self.K1 = numpy.array([ [c1, c2], [c1 * b, -c2 * (l - b)] ])
     self.C1 = numpy.array([ [a1, a2], [a1 * b, -a2 * (l - b)] ])
     self.T = l / v
     self.v = v

   def input_psd(self, omega):
     return self.as1 * self.v / ( 2 * math.pi * (pow(omega,2) + self.bs1 * pow(self.v,2)))


if __name__ == "__main__":
   print("Random Vibration Analysis:")
   data = {} ##contains input data for the analysis

   if len(sys.argv) >= 2:
    input_file = sys.argv[1]
    with open(input_file,"r") as fh:
      while True:
        line = fh.readline()
        if line:
          #####print(line)
          words = line.split(",")
          data[words[0].lower()] = float(words[1])
       
        else:
          break
      truck = Truck(data)
      print()
      print("input PSD:")
      for x in range(101):
        omega = 2 * math.pi * x
        y = truck.input_psd(omega)
        print(omega,y)
      
      print()
      print("Natural frequencies, Hz:")

      a = numpy.dot( numpy.linalg.inv(truck.M), truck.K)
      eigenvalues, eigenvectors = numpy.linalg.eig(a)
      for eig in eigenvalues:
        print(math.sqrt(eig) / (2 * math.pi))

      print()
      print("Mode shapes in columns (normilized to mass matrix):")
      norm = numpy.dot(eigenvectors.T,numpy.dot(truck.M, eigenvectors))
      num_vectors = eigenvectors.shape[1] 
      for i in range(num_vectors):
        eigenvectors[:,i] = eigenvectors[:,i] / math.sqrt(norm[i,i])

      print(eigenvectors)
      ###norm = numpy.dot(eigenvectors.T,numpy.dot(truck.M, eigenvectors))
      ####print(norm)
   else:
    print("no input file")
