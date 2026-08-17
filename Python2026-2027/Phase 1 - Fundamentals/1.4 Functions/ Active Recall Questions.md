Conceptual / Active Recall Questions

def greet(): likhne se function turant chal jaata hai kya, ya sirf define hota hai? Farak samjhao.
def greet(): se sirf define hota hai. 

Parameter aur Argument mein exact farak kya hai?
parameter hum function define krte hue dete hain. and argument function mei pass krte hai call krte time.

print() aur return mein kya farak hai — dono ek jaisa hi kaam karte lagte hain lekin nahi karte, kyun?
print sirf display krta hai but return function ki values ko jahan call kiya gya hai function vahan pe return kr deta hai and we can further use it in our code.

Default argument ke roop mein mutable object (jaise [] ya {}) kyun dangerous hota hai? Kya problem aati hai?
kyunki jab function call hota hai and koe argument pass nhi kiya for list or dict toh ek he list update hoti rheti hai instead of getting created everytime.

*args aur **kwargs mein kya farak hai — konsa kis type ka data collect karta hai?
*args is used when we dont know the count for the arguments that user can pass. 
**kwargs is used when we dont know the the count of key value pairs the user can pass

Function ke andar agar tum ek variable ko bina global keyword ke assign karo jiska naam bahar bhi exist karta hai, toh kya hoga?
kuch nhi hoga andar ek or create ho jayega jiski value sirf ussi function ke andar exist karegi and function ke bahar global vali value he use hogi.

Recursion mein "base case" itna zaroori kyun hai? Agar woh na ho toh kya hoga?
agar base case nhi hua recursion mei toh voh kabhi stop he nhi hoga and ek infinite loop ki tarah chalta rhega

Lambda function normal def function se kaise limited hai — kya cheezein lambda mein nahi likh sakte?
lambda single line single use functions ke liye hota hai. mostly arguments mei use kiye jaate hain and lambda mei hum complex functions and if else nhi kr sakte. ternary operator use kr sakte hain