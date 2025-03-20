#Don't Repeat Yourself (DRY) Prensibi:
#Bu prensip, kodda tekrarların önlenmesi gerektiğini ifade eder. Aynı mantığı veya kodu birden fazla
yerde tekrarlamak yerine, onu bir yerde tanımlayıp gerektiğindekullanmak daha iyi bir yazılım pratiğidir.
Bu sayede kodun bakımı daha kolay olur, hataların önüne geçilir ve kod tekrar kullanımına olanak sağlanır.)

def calculate_area(shape, *dimensions):
    if shape == 'rectangle' and len(dimensions) == 2:
        return dimensions[0] * dimensions[1]
    elif shape == 'square' and len(dimensions) == 1:
        return dimensions[0] * dimensions[0]
    elif shape == 'circle' and len(dimensions) == 1:
        import math
        return math.pi * dimensions[0] * dimensions[0]
    else:
        return "Invalid shape or dimensions"

# Dinamik veri girişi
while True:
    shape = input("Enter the shape (rectangle, square, circle) or 'exit' to quit: ").lower()
    if shape == 'exit':
        break
    dimensions = input("Enter dimensions (separated by space): ").split()

    # Boyutları sayıya dönüştür
    dimensions = [float(d) for d in dimensions]

    area = calculate_area(shape, *dimensions)
    print(f"The area of the {shape} is: {area}")
