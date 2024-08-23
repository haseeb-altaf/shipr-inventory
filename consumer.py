from main import redis, Product
import time

key = "order_completed"
group = "inventry-group"

try:
    redis.xgroup_create(key, group)
except:
    print("Group already exists, skipping creation")

while True:
    try:
        results = redis.xreadgroup(group, key, {key: ">"}, None)
        
        if results != []:
            for result in results:
                obj = result[1][0][1]

                try:
                    product = Product.get(obj['product_id'])
                    print (product)
                    product.stock -= int(obj['quantity'])
                    product.save()
                    print(f"Order {obj['pk']} completed. Updated stock for product {obj['product_id']} to {product.stock}")
                except:
                    redis.xadd("refund_order", obj,'*')
                
    except Exception as e:
        print(str(e))

    time.sleep(5)