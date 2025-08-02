import streamlit as st
import pandas as pd

def find_matching_words_list(Dictionary, text_search):

	Accuracy_Rate = {"Word" : [], "Accuracy" : []}

	for word in range(len(Dictionary)):

		Accuracy_Rate = 0
		if len(Dictionary[word]) > len(text_search):
			for alphabet in range(len(text_search)):

				word1 = text_search[alphabet]
				word2 = alphabet[alphabet]

				if word1 == word2:
					Accuracy_Rate += (100/len(text_search))

		else:
			for alphabet in range(len(Dictionary[word])):

				word1 = text_search[alphabet]
				word2 = alphabet[alphabet]

				if word1 == word2:
					Accuracy_Rate += (100/len(text_search))
				
		Accuracy_Rate["Word"].append(word)
		Accuracy_Rate["Accuracy"].append(Accuracy_Rate)
	
	return Accuracy_Rate

data = pd.read_excel("3D_Character_List_Store.xlsx", engine="openpyxl")

text_search = st.text_input("Search Character do you want to search : ", value="")

searching_Character = data["3D_Character"].str.contains(text_search.capitalize())
# Ini dibuat spelling correction tapi bukan spelling correction melainkan ada lagi lebih ke string matching 
store_Character = data["3D_Character"]
store_Character_List = [i for i in store_Character.values.tolist()]

st.write(store_Character_List)

Character_find = data[searching_Character]

if text_search:
	st.write(Character_find)

N_cards_per_row = 3
if text_search:
	for n_row, row in Character_find.reset_index().iterrows():
		i = n_row%N_cards_per_row
		if i==0:
			st.write("---")
			cols = st.columns(N_cards_per_row, gap="large")
		# draw the card
		with cols[n_row%N_cards_per_row]:
			st.caption(f"{row['3D_Character'].strip()} - {row['3D_Character_Type'].strip()} - {row['3D_Character_Format'].strip()} ")
			# Isinya gambar & Description Gambar
			st.markdown(f"**{row['3D_Character'].strip()}**")
			# st.markdown(f"*{row['Título'].strip()}*")
			# st.markdown(f"**{row['Video']}**")
		if cols[n_row%N_cards_per_row] == 0:
			st.write("The searching are not found.")
else:
	find_matching_words = store_Character_List
	# Gini sih aku nangkep nya store kata list 
	# cari huruf nya kalau akurasi ketepatannya lebih dari 65 %
	# 2 huruf sama => 50 %
	# 3 huruf mirip => 66 %
	# 4 huruf mirip => 75 %
	# 5 huruf mirip => 80 %
	# 6 huruf mirip => 83 %
	st.write(find_matching_words_list(find_matching_words, text_search))