product_name = "Smartphone"
price = 750
is_sale = False
is_available = True
category = ""

if not is_available:
  print(f"Товар {product_name} тимчасово відсутній на складі.")
else:
  if price <= 500 or is_sale:
    category = "Budget / Promotional"
  elif 501 <= price <= 1000:
    category = "Standard"
  else:
    category = "Premium"

  print(
      f"Товар: {product_name}, Ціна: {price} грн, Категорія товару: {category}"
  )