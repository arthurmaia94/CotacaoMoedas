#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2021 Arthur Maia <contato.94tech@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
	def build(self):
		return GUI
	
	def on_start(self):
		self.root.ids["moeda1"].text = f"Dólar R${self.pegarCotacao('USD')}"
		self.root.ids["moeda2"].text = f"Euro R${self.pegarCotacao('EUR')}"
		self.root.ids["moeda3"].text = f"Bitcoin R${self.pegarCotacao('BTC')}"
		self.root.ids["moeda4"].text = f"Etherium R${self.pegarCotacao('ETH')}"
		
	def pegarCotacao(self, moeda):
		link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
		requisicao = requests.get(link)
		dic_requisicao = requisicao.json()
		cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
		return cotacao
		
MeuAplicativo().run()
