
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALPHA BETA COS DELTA DIVIDE FRAC GAMMA IIINT IINT INT LBRACE LOG LPAREN MINUS NUMBER PI PLUS RBRACE RPAREN SIN SQRT SUP TAN TIMES VARIABLEexpression : expression PLUS term\n                  | expression MINUS termexpression : termterm : term TIMES factor\n            | term DIVIDE factorterm : factorfactor : NUMBERfactor : VARIABLEfactor : LPAREN expression RPARENfactor : SIN LPAREN expression RPAREN\n              | COS LPAREN expression RPAREN\n              | TAN LPAREN expression RPARENfactor : LOG LPAREN expression RPARENfactor : SQRT LBRACE expression RBRACEfactor : FRAC LBRACE expression RBRACE LBRACE expression RBRACEfactor : INT factorfactor : INT LBRACE expression RBRACE SUP LBRACE expression RBRACE expressionfactor : IINT LBRACE expression RBRACE SUP LBRACE expression RBRACE expressionfactor : IIINT LBRACE expression RBRACE SUP LBRACE expression RBRACE expressionfactor : ALPHAfactor : BETAfactor : GAMMAfactor : DELTAfactor : PI'
    
_lr_action_items = {'NUMBER':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'VARIABLE':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'LPAREN':([0,6,7,8,9,10,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[6,6,26,27,28,29,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'SIN':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'COS':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'TAN':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'LOG':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'SQRT':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'FRAC':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'INT':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'IINT':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'IIINT':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'ALPHA':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'BETA':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'GAMMA':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'DELTA':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'PI':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'$end':([1,2,3,4,5,16,17,18,19,20,32,36,37,38,39,40,50,51,52,53,54,67,74,75,76,],[0,-3,-6,-7,-8,-20,-21,-22,-23,-24,-16,-1,-2,-4,-5,-9,-10,-11,-12,-13,-14,-15,-17,-18,-19,]),'PLUS':([1,2,3,4,5,16,17,18,19,20,25,32,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,63,67,68,69,70,74,75,76,],[21,-3,-6,-7,-8,-20,-21,-22,-23,-24,21,-16,-1,-2,-4,-5,-9,21,21,21,21,21,21,21,21,21,-10,-11,-12,-13,-14,21,-15,21,21,21,21,21,21,]),'MINUS':([1,2,3,4,5,16,17,18,19,20,25,32,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,63,67,68,69,70,74,75,76,],[22,-3,-6,-7,-8,-20,-21,-22,-23,-24,22,-16,-1,-2,-4,-5,-9,22,22,22,22,22,22,22,22,22,-10,-11,-12,-13,-14,22,-15,22,22,22,22,22,22,]),'RPAREN':([2,3,4,5,16,17,18,19,20,25,32,36,37,38,39,40,41,42,43,44,50,51,52,53,54,67,74,75,76,],[-3,-6,-7,-8,-20,-21,-22,-23,-24,40,-16,-1,-2,-4,-5,-9,50,51,52,53,-10,-11,-12,-13,-14,-15,-17,-18,-19,]),'RBRACE':([2,3,4,5,16,17,18,19,20,32,36,37,38,39,40,45,46,47,48,49,50,51,52,53,54,63,67,68,69,70,74,75,76,],[-3,-6,-7,-8,-20,-21,-22,-23,-24,-16,-1,-2,-4,-5,-9,54,55,56,57,58,-10,-11,-12,-13,-14,67,-15,71,72,73,-17,-18,-19,]),'TIMES':([2,3,4,5,16,17,18,19,20,32,36,37,38,39,40,50,51,52,53,54,67,74,75,76,],[23,-6,-7,-8,-20,-21,-22,-23,-24,-16,23,23,-4,-5,-9,-10,-11,-12,-13,-14,-15,-17,-18,-19,]),'DIVIDE':([2,3,4,5,16,17,18,19,20,32,36,37,38,39,40,50,51,52,53,54,67,74,75,76,],[24,-6,-7,-8,-20,-21,-22,-23,-24,-16,24,24,-4,-5,-9,-10,-11,-12,-13,-14,-15,-17,-18,-19,]),'LBRACE':([11,12,13,14,15,55,60,61,62,],[30,31,33,34,35,59,64,65,66,]),'SUP':([56,57,58,],[60,61,62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,6,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[1,25,41,42,43,44,45,46,47,48,49,63,68,69,70,74,75,76,]),'term':([0,6,21,22,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[2,2,36,37,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'factor':([0,6,13,21,22,23,24,26,27,28,29,30,31,33,34,35,59,64,65,66,71,72,73,],[3,3,32,3,3,38,39,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_binop','parser.py',5),
  ('expression -> expression MINUS term','expression',3,'p_expression_binop','parser.py',6),
  ('expression -> term','expression',1,'p_expression_term','parser.py',10),
  ('term -> term TIMES factor','term',3,'p_term_binop','parser.py',14),
  ('term -> term DIVIDE factor','term',3,'p_term_binop','parser.py',15),
  ('term -> factor','term',1,'p_term_factor','parser.py',23),
  ('factor -> NUMBER','factor',1,'p_factor_number','parser.py',27),
  ('factor -> VARIABLE','factor',1,'p_factor_variable','parser.py',31),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parser.py',35),
  ('factor -> SIN LPAREN expression RPAREN','factor',4,'p_factor_trig','parser.py',39),
  ('factor -> COS LPAREN expression RPAREN','factor',4,'p_factor_trig','parser.py',40),
  ('factor -> TAN LPAREN expression RPAREN','factor',4,'p_factor_trig','parser.py',41),
  ('factor -> LOG LPAREN expression RPAREN','factor',4,'p_factor_log','parser.py',50),
  ('factor -> SQRT LBRACE expression RBRACE','factor',4,'p_factor_sqrt','parser.py',54),
  ('factor -> FRAC LBRACE expression RBRACE LBRACE expression RBRACE','factor',7,'p_factor_frac','parser.py',58),
  ('factor -> INT factor','factor',2,'p_factor_int_simple','parser.py',69),
  ('factor -> INT LBRACE expression RBRACE SUP LBRACE expression RBRACE expression','factor',9,'p_factor_int_with_limits','parser.py',73),
  ('factor -> IINT LBRACE expression RBRACE SUP LBRACE expression RBRACE expression','factor',9,'p_factor_iint_with_limits','parser.py',88),
  ('factor -> IIINT LBRACE expression RBRACE SUP LBRACE expression RBRACE expression','factor',9,'p_factor_iiint_with_limits','parser.py',103),
  ('factor -> ALPHA','factor',1,'p_factor_alpha','parser.py',118),
  ('factor -> BETA','factor',1,'p_factor_beta','parser.py',122),
  ('factor -> GAMMA','factor',1,'p_factor_gamma','parser.py',126),
  ('factor -> DELTA','factor',1,'p_factor_delta','parser.py',130),
  ('factor -> PI','factor',1,'p_factor_pi','parser.py',134),
]