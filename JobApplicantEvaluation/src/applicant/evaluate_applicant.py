from utilities.evaluation_result import EvaluationResult

import os, pkgutil
import importlib

def get_criteria():
  criteria = list(file_name.replace('_', " ").title()
    for _, file_name, _ in pkgutil.iter_modules(
    [os.path.join(os.path.dirname(os.path.dirname(__file__)), 'evaluate')]))
  return {criterion: get_criterion_check(criterion) for criterion in criteria}

def get_selected_criteria(criteria):
  return {criterion: get_criteria()[criterion] for criterion in criteria}

def get_criterion_check(criterion):
  return importlib.import_module(
    '.' + criterion.lower().replace(' ', '_'), package = 'evaluate')

def evaluate_applicant(applicant, criteria):
  if not criteria:
    return (EvaluationResult.FAIL, 'No criteria was provided')
  
  applicant_status_list = list(map(lambda selected_criteria: selected_criteria.check(applicant),
    get_selected_criteria(criteria).values()))
  
  return (EvaluationResult.FAIL \
    if EvaluationResult.FAIL in list(map(lambda applicant_status: applicant_status[0], applicant_status_list)) \
    else EvaluationResult.PASS,
  ', '.join(list(map(lambda applicant_status: applicant_status[1], applicant_status_list))))
