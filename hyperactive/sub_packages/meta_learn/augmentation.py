'''
MIT License
Copyright (c) [2018] [Simon Franz Albert Blanke]
Email: simonblanke528481@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import time
import datetime
import numpy as np
import pandas as pd
from tqdm import tqdm
import multiprocessing

num_cores = multiprocessing.cpu_count()

class Dataset_augmentation(object):
	def __init__(self):
		pass



	def drop_all_features_once(self, X_train, y_train, dataset_name='dataset'):
		aug_dataset_dict = {}

		aug_dataset_dict[dataset_name] = X_train

		aug_dataset_dict_temp = dict(aug_dataset_dict)
		aug_dataset_dict[dataset_name] = [X_train, y_train]

		aug_dataset_dict_temp = self._drop_features(aug_dataset_dict_temp)

		for key_temp in aug_dataset_dict_temp:
			aug_dataset_dict[key_temp] = [aug_dataset_dict_temp[key_temp], y_train]

		print(aug_dataset_dict.keys())
		return aug_dataset_dict


	def _correct_n_drops(self, X_train, n_drops):
		if n_drops > len(X_train.columns)-2:
			n_drops = len(X_train.columns)-2
			print('Number of drops to high for dataset. Setting n_drops to', n_drops)

		return n_drops


	def _drop_features(self, aug_dataset_dict, n_at_a_time=2):
		dataset_dict_temp = {}

		for dataset_key in tqdm(aug_dataset_dict):
			dataset = aug_dataset_dict[dataset_key]
			features = dataset.columns


			for feature in features:
				dataset_dropped = dataset
				for drop in range(n_at_a_time):

				dataset_dict_temp[key] = dataset_dropped

		return dataset_dict_temp



	def _drop_feature(self, X_train, feature):

		X_train_dropped = X_train.drop(feature, axis=1)
		key = dataset_key+'_'+str(feature)

		return key, X_train_dropped




	def _drop_instance(self, dataset_dict):
		dataset_dict_temp = {}
		already_dropped = []

		for dataset_key in dataset_dict:
			dataset = dataset_dict[dataset_key][0]
			rows = dataset.index

			for row in rows:
				dataset_dropped = dataset.drop(row, axis=0)
				append = True
				for dropped_rows in already_dropped:
					if dropped_rows == list(dataset_dropped.index):
						append = False

				already_dropped.append(list(dataset_dropped.index))
				if append == True:
					key = dataset_key+'_'+str(row)
					dataset_dict_temp[key] = dataset_dropped

		return dataset_dict_temp