sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
history = sample_dict["class"]["student"]["marks"]["history"]
print (history)

thing = {"one":"a", "two": "b"}
print("one" in thing)
del thing["one"]
print("one" in thing)
print(thing)

