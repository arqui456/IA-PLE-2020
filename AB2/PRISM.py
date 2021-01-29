import numpy as np
import pandas as pd
from dfply import *

#Exemplo de algoritmo PRISM para regras de associação

def compute_probabilities(df, target):
	prob_table = pd.DataFrame()
	feature_matrix = df.drop(target, axis=1)
	feature_variables = feature_matrix.columns.values
	target_variable = target

	for feature_variable in feature_variables:
		for unique_value in feature_matrix[feature_variable].unique():
			prob_table = prob_table.append((df 	>> mask(X[feature_variable] == unique_value)
												>> group_by(X[target_variable])
											   	>> summarize(count = n(X[target_variable]))
											   	>> ungroup()
											   	>> rename(target = X[target_variable])
											   	>> mutate(probability = X['count']/X['count'].sum())
											   	>> mutate(variable = feature_variable)
											   	>> mutate(value = unique_value)
											   	>> select(['target', 'variable', 'value', 'probability'])), ignore_index=True)
	return prob_table

def return_best_rule(prob_table):
	best_rule = prob_table >> mask(X['probability'] == X['probability'].max())
	return best_rule.iloc[0, :]

def update_table(prob_table, rule):
	for idx in prob_table.index:
		if prob_table.iloc[idx,:].equals(rule):
			new_table = prob_table.drop(idx).reset_index(drop=True)
	return new_table

def PRISM(df, target):
	rules = []
	prob_table = compute_probabilities(df, target)
	print(prob_table)
	while prob_table.empty == False:
		best_rule = return_best_rule(prob_table)
		rules.append(best_rule['variable']+' == '+best_rule['value'])
		prob_table = update_table(prob_table, best_rule)
	return rules

data = {
	'age' : ['Young', 'Young', 'Young', 'Young', 'Young', 'Young', 'Young', 'Young', 
			 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic',
			 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic'],
	'prescription': ['Myope', 'Myope', 'Myope', 'Myope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope',
					 'Myope', 'Myope', 'Myope', 'Myope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope',
					 'Myope', 'Myope', 'Myope', 'Myope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope'],
	'astigmatism': ['Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes',
					'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes'],
	'tear rate': ['Normal', 'Reduced', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced',
				  'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal',
				  'Reduced', 'Normal'],
	'teste': ['Hard', 'None', 'None', 'Soft', 'None', 'Soft', 'None', 'Hard', 'None', 'Soft', 'None', 'Hard', 'None', 'Soft',
			  'None', 'None', 'None', 'None', 'None', 'Hard', 'None', 'Soft', 'None', 'None']
	}

df = pd.DataFrame(data)

rules = PRISM(df, 'teste')

#imprimindo a lista de regras associativas que por padrão já estão em ordem crescente de importância.
print(rules)