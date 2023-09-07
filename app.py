class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def add(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return ComplexNumber(real_part, imag_part)

    def subtract(self, other):
        real_part = self.real - other.real
        imag_part = self.imag - other.imag
        return ComplexNumber(real_part, imag_part)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def divide(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag

# Exemplo de uso:
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, -2)

print("Número 1:", num1)
print("Número 2:", num2)

result_add = num1.add(num2)
print("Soma:", result_add)

result_subtract = num1.subtract(num2)
print("Subtração:", result_subtract)

result_multiply = num1.multiply(num2)
print("Multiplicação:", result_multiply)

result_divide = num1.divide(num2)
print("Divisão:", result_divide)

print("Parte Real de Número 1:", num1.get_real())
print("Parte Imaginária de Número 1:", num1.get_imag())
