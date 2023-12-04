def fibo (n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

fiboNum = [fibo(i) for i in range(20)]
print(fiboNum)

# Export the result to a text file
output_file_path = '/root/cGPT_wo_NN/input.txt'
with open(output_file_path, 'w') as file:
      file.write(','.join(map(str, fiboNum)))

print(f"Result has been exported to {output_file_path}")