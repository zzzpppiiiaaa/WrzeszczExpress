# def spawn_train():
#
#     train_type = random.choice(["R","R", "TLK", "IC", "EIP/EIC", "cargo", "SKM", "SKM","SKM"])
#     if train_type == "R":
#         number = random.choice(["55", "50", "59", "95", "96", "97"]) + str(random.randint(100, 999))
#         direction = random.choice(["Gdansk Glowny", "Bretowo", "Sopot"])
#         if direction == "Bretowo": place = "block65"
#
#     elif train_type == "TLK":
#         number = random.randint(10000, 99999)
#         direction = random.choice(["Gdansk Glowny", "Sopot"])
#         if direction == "Gdansk Glowny": place = "block5"
#         else: place = "block??" #POPRAWIĆ BLOKI
#
#     elif train_type == "IC":
#         number = random.randint(1000, 99999)
#         direction = random.choice(["Gdansk Glowny", "Sopot"])
#         if direction == "Gdansk Glowny": place = "block5"
#         else: place = "block??" #POPRAWIĆ BLOKI
#
#     elif train_type == "EIP/EIC":
#         number = random.randint(1000, 9999)
#         direction = random.choice(["Gdansk Glowny", "Sopot"])
#         if direction == "Gdansk Glowny": place = "block5"
#         else: place = "block??" #POPRAWIĆ BLOKI
#
#     elif train_type == "SKM":
#         number = random.choice(["59", "95"]) + str(random.randint(100, 999))
#         direction = random.choice(["Gdansk Glowny SKM", "Gdansk Oliwa"])
#         if direction == "Gdansk Glowny SKM": place = "block11"
#         else: place = "block??" #POPRAWIĆ BLOKI
#     else:
#         number = random.randint(100000, 999999)
#         direction = random.choice(["Gdansk Glowny", "Sopot"])
#         if direction == "Gdansk Glowny": place = "block5"
#         else: place = "block??" #POPRAWIĆ BLOKI
#
#
#     trains.append(Train(number, place, blocks, direction))
