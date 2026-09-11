#Write a program to generate a random OTP. Ask user to enter the no of digits(4 or 6) required for the otp. Generate the otp and print it
n = int(input("Enter number of terms: "))
a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(3, n + 1):
 c = a + b
 print(c, end=" ")
 a = b
 b = c