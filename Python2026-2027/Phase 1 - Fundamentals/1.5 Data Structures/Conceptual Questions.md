List aur Tuple mein sabse bada functional farak kya hai — kab kaunsa use karoge?
List is mutable. tuple is immutable. list when we want the data to be edited or updated. tuple when we want data security and not to be updated.

list[2:5] mein index 5 wala element include hota hai kya? Predict karo nums = [0,1,2,3,4,5,6,7,8,9] ke liye nums[2:5] ka output.
no its not included. output 2,3,4

nums[::-1] kya karta hai — step ka role kya hai yahan?
reverses. default (first) : default(last) included : -1 goes 1 back at a time

Dictionary mein .get() aur [] (square brackets) se value nikaalne mein kya farak hai — kaunsa safer hai aur kyun?
.get handles safely if the key doesnt exist. [] crashes if key doesnt exist

Set mein duplicate values kyun automatically hat jaati hain?
because its a property of set that its unique 

(5) aur (5,) mein Python ke liye kya farak hai?
(5) just an integer with () .. (5, ) is a single element tuple.

Nested data structure ka ek real-world example socho (jaise list of dictionaries) — aur bataओ ise access karne ka logic kaise sochte ho step-by-step.
first list element  which gives access to dictionary, then fetch dictionary values via key .get.