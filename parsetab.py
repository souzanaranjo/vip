
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND ASSIGN COLON COMMA CONST_F CONST_I CONST_STRING DIVIDE ELIF ELSE EQUALS FLOAT FUNCTION GLOBAL GREATER GREATER_EQ ID IF INT LESS LESS_EQ L_KEY_BRACKET L_PARENS L_SQUARE_BRACKET MAIN MINUS NOT NOT_EQUAL OR PLUS PRINT READ RETURN R_KEY_BRACKET R_PARENS R_SQUARE_BRACKET SEMICOLON STRING TIMES VOID WHILEprogram : program_aux main\n               | mainprogram_aux : program_aux function\n                   | functionfunction : function_header function_body n_end_functionmain : FUNCTION MAIN n_start_main function_body n_end_functionfunction_header : FUNCTION ID n_add_function_name L_PARENS function_params R_PARENS COLON function_type\n                       | FUNCTION ID n_add_function_name L_PARENS R_PARENS COLON function_typefunction_body : L_KEY_BRACKET function_body_aux statements R_KEY_BRACKET\n                     | L_KEY_BRACKET statements R_KEY_BRACKETfunction_body_aux : var function_body_aux\n                         | varstatements : statement statements\n                           | statementfunction_params : type ID n_add_var array_index COMMA function_params\n                       | type ID n_add_var array_index\n                       | type ID n_add_var COMMA function_params\n                       | type ID n_add_varfunction_type : INT n_add_function_type\n                     | FLOAT n_add_function_type\n                     | STRING n_add_function_type\n                     | VOID n_add_function_typevar : type_aux ID n_add_var array_dim var_aux SEMICOLON\n           | type_aux ID n_add_var array_dim SEMICOLON\n           | type_aux ID n_add_var var_aux SEMICOLON\n           | type_aux ID n_add_var SEMICOLONtype_aux : GLOBAL type\n                | typevar_aux : COMMA ID n_add_var array_dim var_aux\n               | COMMA ID n_add_var array_dim\n               | COMMA ID n_add_var var_aux\n               | COMMA ID n_add_varstatement : statement_aux SEMICOLON\n                 | statement_aux_2statement_aux : assignment\n                     | function_call\n                     | return\n                     | printstatement_aux_2 : if\n                       | whiletype : INT n_record_last_type\n            | FLOAT n_record_last_type\n            | STRING n_record_last_typearray_index : L_SQUARE_BRACKET expression R_SQUARE_BRACKET L_SQUARE_BRACKET expression R_SQUARE_BRACKET\n                   | L_SQUARE_BRACKET expression R_SQUARE_BRACKETarray_dim : L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET\n                 | L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKETassignment : ID n_add_operand array_index ASSIGN n_make_assignment expression\n                  | ID n_add_operand array_index ASSIGN n_make_assignment read\n                  | ID n_add_operand ASSIGN n_make_assignment expression\n                  | ID n_add_operand ASSIGN n_make_assignment readfunction_call : ID params_passreturn : RETURN expressionif : IF L_PARENS expression R_PARENS block elif else\n          | IF L_PARENS expression R_PARENS block elif\n          | IF L_PARENS expression R_PARENS block else\n          | IF L_PARENS expression R_PARENS blockelif : ELIF L_PARENS expression R_PARENS block elif\n            | ELIF L_PARENS expression R_PARENS blockelse : ELSE blockwhile : WHILE L_PARENS expression R_PARENS blockprint : PRINT L_PARENS print_aux R_PARENS\n             | PRINT L_PARENS R_PARENSprint_aux : CONST_STRING COMMA print_aux\n                 | CONST_STRING\n                 | ID COMMA print_aux\n                 | IDexpression : exp n_eval_exp AND n_add_operator expression\n                  | exp n_eval_expread : READ IDparams_pass : L_PARENS expression params_pass_aux R_PARENS\n                   | L_PARENS expression R_PARENS\n                   | L_PARENS R_PARENSparams_pass_aux : COMMA expression params_pass_aux\n                       | COMMA expressionblock : L_KEY_BRACKET statements R_KEY_BRACKETexp : xp n_eval_xp OR n_add_operator exp\n           | xp n_eval_xpxp : x n_eval_x log_op n_add_operator x\n          | x n_eval_xx : term n_eval_term x_aux\n         | term n_eval_termx_aux : PLUS n_add_operator term x_aux\n             | PLUS n_add_operator term\n             | MINUS n_add_operator term x_aux\n             | MINUS n_add_operator termlog_op : NOT_EQUAL\n              | EQUALS\n              | GREATER\n              | GREATER_EQ\n              | LESS\n              | LESS_EQterm : factor n_eval_factor term_aux\n            | factor n_eval_factorterm_aux : TIMES n_add_operator factor term_aux\n                | TIMES n_add_operator factor\n                | DIVIDE n_add_operator factor term_aux\n                | DIVIDE n_add_operator factorfactor : NOT factor_aux\n              | factor_auxfactor_aux : L_PARENS expression R_PARENS\n                  | PLUS const\n                  | MINUS const\n                  | constconst : ID n_add_operand\n             | CONST_I n_add_operand\n             | CONST_F n_add_operand\n             | CONST_STRING n_add_operand\n             | function_call\n             | array_accessarray_access : ID array_indexn_start_main : n_add_function_name : n_add_function_type : n_end_function : n_add_var : n_record_last_type : n_eval_exp : n_eval_xp : n_eval_x : n_eval_factor : n_eval_term : n_add_operand : n_add_operator : n_make_assignment : '
    
_lr_action_items = {'FUNCTION':([0,2,4,8,11,15,42,79,],[5,5,-4,-3,-115,-5,-10,-9,]),'$end':([1,3,7,39,42,75,79,],[0,-2,-1,-115,-10,-6,-9,]),'MAIN':([5,],[9,]),'ID':([5,12,16,18,19,20,23,25,30,31,32,33,34,35,43,48,49,50,51,52,53,60,62,63,65,72,73,74,78,82,83,111,113,114,115,119,120,121,122,123,124,125,126,127,128,130,131,133,134,137,138,149,150,153,156,160,161,162,163,164,165,166,169,170,171,179,185,194,195,209,210,211,212,220,221,],[10,21,21,-12,21,45,-34,-28,-39,-40,-117,-117,-117,66,-11,66,-33,-27,-41,-42,-43,66,66,66,66,103,66,66,108,-125,66,-26,152,-125,66,66,-124,-124,-124,-87,-88,-89,-90,-91,-92,-124,-124,-124,-124,103,103,-24,-25,66,184,66,66,66,66,66,66,66,-57,21,-61,-23,66,-55,-56,-54,66,-60,-76,-59,-58,]),'L_KEY_BRACKET':([6,9,13,139,140,142,143,144,145,146,172,173,174,175,176,197,219,],[12,-112,12,170,170,-8,-114,-114,-114,-114,-7,-19,-20,-21,-22,170,170,]),'L_PARENS':([10,14,21,35,36,37,38,48,60,62,66,73,74,82,83,114,115,119,120,121,122,123,124,125,126,127,128,130,131,133,134,153,160,161,162,163,164,165,166,185,196,210,],[-113,40,48,62,72,73,74,62,62,62,48,62,62,-125,62,-125,62,62,-124,-124,-124,-87,-88,-89,-90,-91,-92,-124,-124,-124,-124,62,62,62,62,62,62,62,62,62,210,62,]),'GLOBAL':([12,18,111,149,150,179,],[24,24,-26,-24,-25,-23,]),'INT':([12,18,24,40,107,111,141,149,150,178,179,199,],[32,32,32,32,143,-26,143,-24,-25,32,-23,32,]),'FLOAT':([12,18,24,40,107,111,141,149,150,178,179,199,],[33,33,33,33,144,-26,144,-24,-25,33,-23,33,]),'STRING':([12,18,24,40,107,111,141,149,150,178,179,199,],[34,34,34,34,145,-26,145,-24,-25,34,-23,34,]),'RETURN':([12,16,18,19,23,30,31,43,49,111,149,150,169,170,171,179,194,195,209,211,212,220,221,],[35,35,-12,35,-34,-39,-40,-11,-33,-26,-24,-25,-57,35,-61,-23,-55,-56,-54,-60,-76,-59,-58,]),'PRINT':([12,16,18,19,23,30,31,43,49,111,149,150,169,170,171,179,194,195,209,211,212,220,221,],[36,36,-12,36,-34,-39,-40,-11,-33,-26,-24,-25,-57,36,-61,-23,-55,-56,-54,-60,-76,-59,-58,]),'IF':([12,16,18,19,23,30,31,43,49,111,149,150,169,170,171,179,194,195,209,211,212,220,221,],[37,37,-12,37,-34,-39,-40,-11,-33,-26,-24,-25,-57,37,-61,-23,-55,-56,-54,-60,-76,-59,-58,]),'WHILE':([12,16,18,19,23,30,31,43,49,111,149,150,169,170,171,179,194,195,209,211,212,220,221,],[38,38,-12,38,-34,-39,-40,-11,-33,-26,-24,-25,-57,38,-61,-23,-55,-56,-54,-60,-76,-59,-58,]),'R_KEY_BRACKET':([17,19,23,30,31,41,44,49,169,171,194,195,198,209,211,212,220,221,],[42,-14,-34,-39,-40,79,-13,-33,-57,-61,-55,-56,212,-54,-60,-76,-59,-58,]),'ASSIGN':([21,46,81,157,216,],[-123,82,114,-45,-44,]),'L_SQUARE_BRACKET':([21,45,46,66,80,108,147,152,157,180,181,],[-123,-116,83,83,112,-116,83,-116,185,201,112,]),'SEMICOLON':([22,26,27,28,29,45,47,54,55,56,57,58,59,61,64,66,67,68,69,70,71,80,85,86,87,88,89,90,91,93,94,95,96,97,98,99,101,109,110,118,129,132,135,136,148,152,154,155,157,158,180,181,182,183,184,187,188,189,190,191,192,193,202,203,205,206,207,208,215,216,218,],[49,-35,-36,-37,-38,-116,-52,-53,-118,-119,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,111,-73,-69,-78,-80,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,-63,149,150,-72,-81,-93,-101,-62,179,-116,-50,-51,-45,-71,-47,-32,-48,-49,-70,-68,-77,-79,-84,-86,-96,-98,-30,-31,-83,-85,-95,-97,-29,-44,-46,]),'NOT':([35,48,62,73,74,82,83,114,115,119,120,121,122,123,124,125,126,127,128,130,131,133,134,153,160,161,162,163,164,165,166,185,210,],[60,60,60,60,60,-125,60,-125,60,60,-124,-124,-124,-87,-88,-89,-90,-91,-92,-124,-124,-124,-124,60,60,60,60,60,60,60,60,60,60,]),'PLUS':([35,47,48,58,59,60,61,62,64,66,67,68,69,70,71,73,74,82,83,85,89,90,91,93,94,95,96,97,98,99,114,115,118,119,120,121,122,123,124,125,126,127,128,130,131,132,133,134,135,153,157,158,160,161,162,163,164,165,166,185,190,191,192,193,207,208,210,216,],[63,-52,63,-122,-121,63,-100,63,-104,-123,-123,-123,-123,-109,-110,63,63,-125,63,-73,130,-94,-99,-102,-103,-105,-111,-106,-107,-108,-125,63,-72,63,-124,-124,-124,-87,-88,-89,-90,-91,-92,-124,-124,-93,-124,-124,-101,63,-45,-71,63,63,63,63,63,63,63,63,130,130,-96,-98,-95,-97,63,-44,]),'MINUS':([35,47,48,58,59,60,61,62,64,66,67,68,69,70,71,73,74,82,83,85,89,90,91,93,94,95,96,97,98,99,114,115,118,119,120,121,122,123,124,125,126,127,128,130,131,132,133,134,135,153,157,158,160,161,162,163,164,165,166,185,190,191,192,193,207,208,210,216,],[65,-52,65,-122,-121,65,-100,65,-104,-123,-123,-123,-123,-109,-110,65,65,-125,65,-73,131,-94,-99,-102,-103,-105,-111,-106,-107,-108,-125,65,-72,65,-124,-124,-124,-87,-88,-89,-90,-91,-92,-124,-124,-93,-124,-124,-101,65,-45,-71,65,65,65,65,65,65,65,65,131,131,-96,-98,-95,-97,65,-44,]),'CONST_I':([35,48,60,62,63,65,73,74,82,83,112,114,115,119,120,121,122,123,124,125,126,127,128,130,131,133,134,153,160,161,162,163,164,165,166,185,201,210,],[67,67,67,67,67,67,67,67,-125,67,151,-125,67,67,-124,-124,-124,-87,-88,-89,-90,-91,-92,-124,-124,-124,-124,67,67,67,67,67,67,67,67,67,214,67,]),'CONST_F':([35,48,60,62,63,65,73,74,82,83,114,115,119,120,121,122,123,124,125,126,127,128,130,131,133,134,153,160,161,162,163,164,165,166,185,210,],[68,68,68,68,68,68,68,68,-125,68,-125,68,68,-124,-124,-124,-87,-88,-89,-90,-91,-92,-124,-124,-124,-124,68,68,68,68,68,68,68,68,68,68,]),'CONST_STRING':([35,48,60,62,63,65,72,73,74,82,83,114,115,119,120,121,122,123,124,125,126,127,128,130,131,133,134,137,138,153,160,161,162,163,164,165,166,185,210,],[69,69,69,69,69,69,102,69,69,-125,69,-125,69,69,-124,-124,-124,-87,-88,-89,-90,-91,-92,-124,-124,-124,-124,102,102,69,69,69,69,69,69,69,69,69,69,]),'R_PARENS':([40,47,48,55,56,57,58,59,61,64,66,67,68,69,70,71,72,76,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,108,117,118,129,132,135,147,157,158,159,167,168,177,186,187,188,189,190,191,192,193,200,205,206,207,208,213,216,217,],[77,-52,85,-118,-119,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,101,106,118,-73,-69,-78,-80,-82,-94,-99,135,-102,-103,-105,-111,-106,-107,-108,136,-65,-67,139,140,-116,158,-72,-81,-93,-101,-18,-45,-71,-75,-64,-66,-16,-74,-68,-77,-79,-84,-86,-96,-98,-17,-83,-85,-95,-97,-15,-44,219,]),'COMMA':([45,47,55,56,57,58,59,61,64,66,67,68,69,70,71,80,84,85,86,87,88,89,90,91,93,94,95,96,97,98,99,102,103,108,109,118,129,132,135,147,152,157,158,159,177,180,181,187,188,189,190,191,192,193,202,205,206,207,208,216,218,],[-116,-52,-118,-119,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,113,119,-73,-69,-78,-80,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,137,138,-116,113,-72,-81,-93,-101,178,-116,-45,-71,119,199,-47,113,-68,-77,-79,-84,-86,-96,-98,113,-83,-85,-95,-97,-44,-46,]),'TIMES':([47,59,61,64,66,67,68,69,70,71,85,90,91,93,94,95,96,97,98,99,118,135,157,158,192,193,216,],[-52,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,133,-99,-102,-103,-105,-111,-106,-107,-108,-72,-101,-45,-71,133,133,-44,]),'DIVIDE':([47,59,61,64,66,67,68,69,70,71,85,90,91,93,94,95,96,97,98,99,118,135,157,158,192,193,216,],[-52,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,134,-99,-102,-103,-105,-111,-106,-107,-108,-72,-101,-45,-71,134,134,-44,]),'NOT_EQUAL':([47,57,58,59,61,64,66,67,68,69,70,71,85,88,89,90,91,93,94,95,96,97,98,99,118,129,132,135,157,158,190,191,192,193,205,206,207,208,216,],[-52,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,123,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,-72,-81,-93,-101,-45,-71,-84,-86,-96,-98,-83,-85,-95,-97,-44,]),'EQUALS':([47,57,58,59,61,64,66,67,68,69,70,71,85,88,89,90,91,93,94,95,96,97,98,99,118,129,132,135,157,158,190,191,192,193,205,206,207,208,216,],[-52,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,124,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,-72,-81,-93,-101,-45,-71,-84,-86,-96,-98,-83,-85,-95,-97,-44,]),'GREATER':([47,57,58,59,61,64,66,67,68,69,70,71,85,88,89,90,91,93,94,95,96,97,98,99,118,129,132,135,157,158,190,191,192,193,205,206,207,208,216,],[-52,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,125,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,-72,-81,-93,-101,-45,-71,-84,-86,-96,-98,-83,-85,-95,-97,-44,]),'GREATER_EQ':([47,57,58,59,61,64,66,67,68,69,70,71,85,88,89,90,91,93,94,95,96,97,98,99,118,129,132,135,157,158,190,191,192,193,205,206,207,208,216,],[-52,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,126,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,-72,-81,-93,-101,-45,-71,-84,-86,-96,-98,-83,-85,-95,-97,-44,]),'LESS':([47,57,58,59,61,64,66,67,68,69,70,71,85,88,89,90,91,93,94,95,96,97,98,99,118,129,132,135,157,158,190,191,192,193,205,206,207,208,216,],[-52,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,127,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,-72,-81,-93,-101,-45,-71,-84,-86,-96,-98,-83,-85,-95,-97,-44,]),'LESS_EQ':([47,57,58,59,61,64,66,67,68,69,70,71,85,88,89,90,91,93,94,95,96,97,98,99,118,129,132,135,157,158,190,191,192,193,205,206,207,208,216,],[-52,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,128,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,-72,-81,-93,-101,-45,-71,-84,-86,-96,-98,-83,-85,-95,-97,-44,]),'OR':([47,56,57,58,59,61,64,66,67,68,69,70,71,85,87,88,89,90,91,93,94,95,96,97,98,99,118,129,132,135,157,158,189,190,191,192,193,205,206,207,208,216,],[-52,-119,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,121,-80,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,-72,-81,-93,-101,-45,-71,-79,-84,-86,-96,-98,-83,-85,-95,-97,-44,]),'AND':([47,55,56,57,58,59,61,64,66,67,68,69,70,71,85,86,87,88,89,90,91,93,94,95,96,97,98,99,118,129,132,135,157,158,188,189,190,191,192,193,205,206,207,208,216,],[-52,-118,-119,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,120,-78,-80,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,-72,-81,-93,-101,-45,-71,-77,-79,-84,-86,-96,-98,-83,-85,-95,-97,-44,]),'R_SQUARE_BRACKET':([47,55,56,57,58,59,61,64,66,67,68,69,70,71,85,86,87,88,89,90,91,93,94,95,96,97,98,99,116,118,129,132,135,151,157,158,187,188,189,190,191,192,193,204,205,206,207,208,214,216,],[-52,-118,-119,-120,-122,-121,-100,-104,-123,-123,-123,-123,-109,-110,-73,-69,-78,-80,-82,-94,-99,-102,-103,-105,-111,-106,-107,-108,157,-72,-81,-93,-101,180,-45,-71,-68,-77,-79,-84,-86,-96,-98,216,-83,-85,-95,-97,218,-44,]),'COLON':([77,106,],[107,141,]),'READ':([82,114,115,153,],[-125,-125,156,156,]),'VOID':([107,141,],[146,146,]),'ELIF':([169,212,220,],[196,-76,196,]),'ELSE':([169,194,212,220,221,],[197,197,-76,-59,-58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_aux':([0,],[2,]),'main':([0,2,],[3,7,]),'function':([0,2,],[4,8,]),'function_header':([0,2,],[6,6,]),'function_body':([6,13,],[11,39,]),'n_start_main':([9,],[13,]),'n_add_function_name':([10,],[14,]),'n_end_function':([11,39,],[15,75,]),'function_body_aux':([12,18,],[16,43,]),'statements':([12,16,19,170,],[17,41,44,198,]),'var':([12,18,],[18,18,]),'statement':([12,16,19,170,],[19,19,19,19,]),'type_aux':([12,18,],[20,20,]),'statement_aux':([12,16,19,170,],[22,22,22,22,]),'statement_aux_2':([12,16,19,170,],[23,23,23,23,]),'type':([12,18,24,40,178,199,],[25,25,50,78,78,78,]),'assignment':([12,16,19,170,],[26,26,26,26,]),'function_call':([12,16,19,35,48,60,62,63,65,73,74,83,115,119,153,160,161,162,163,164,165,166,170,185,210,],[27,27,27,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,27,70,70,]),'return':([12,16,19,170,],[28,28,28,28,]),'print':([12,16,19,170,],[29,29,29,29,]),'if':([12,16,19,170,],[30,30,30,30,]),'while':([12,16,19,170,],[31,31,31,31,]),'n_add_operand':([21,66,67,68,69,],[46,95,97,98,99,]),'params_pass':([21,66,],[47,47,]),'n_record_last_type':([32,33,34,],[51,52,53,]),'expression':([35,48,62,73,74,83,115,119,153,160,185,210,],[54,84,92,104,105,116,154,159,182,187,204,217,]),'exp':([35,48,62,73,74,83,115,119,153,160,161,185,210,],[55,55,55,55,55,55,55,55,55,55,188,55,55,]),'xp':([35,48,62,73,74,83,115,119,153,160,161,185,210,],[56,56,56,56,56,56,56,56,56,56,56,56,56,]),'x':([35,48,62,73,74,83,115,119,153,160,161,162,185,210,],[57,57,57,57,57,57,57,57,57,57,57,189,57,57,]),'term':([35,48,62,73,74,83,115,119,153,160,161,162,163,164,185,210,],[58,58,58,58,58,58,58,58,58,58,58,58,190,191,58,58,]),'factor':([35,48,62,73,74,83,115,119,153,160,161,162,163,164,165,166,185,210,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,192,193,59,59,]),'factor_aux':([35,48,60,62,73,74,83,115,119,153,160,161,162,163,164,165,166,185,210,],[61,61,91,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'const':([35,48,60,62,63,65,73,74,83,115,119,153,160,161,162,163,164,165,166,185,210,],[64,64,64,64,93,94,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'array_access':([35,48,60,62,63,65,73,74,83,115,119,153,160,161,162,163,164,165,166,185,210,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'function_params':([40,178,199,],[76,200,213,]),'n_add_var':([45,108,152,],[80,147,181,]),'array_index':([46,66,147,],[81,96,177,]),'n_eval_exp':([55,],[86,]),'n_eval_xp':([56,],[87,]),'n_eval_x':([57,],[88,]),'n_eval_term':([58,],[89,]),'n_eval_factor':([59,],[90,]),'print_aux':([72,137,138,],[100,167,168,]),'array_dim':([80,181,],[109,202,]),'var_aux':([80,109,181,202,],[110,148,203,215,]),'n_make_assignment':([82,114,],[115,153,]),'params_pass_aux':([84,159,],[117,186,]),'log_op':([88,],[122,]),'x_aux':([89,190,191,],[129,205,206,]),'term_aux':([90,192,193,],[132,207,208,]),'function_type':([107,141,],[142,172,]),'read':([115,153,],[155,183,]),'n_add_operator':([120,121,122,130,131,133,134,],[160,161,162,163,164,165,166,]),'block':([139,140,197,219,],[169,171,211,220,]),'n_add_function_type':([143,144,145,146,],[173,174,175,176,]),'elif':([169,220,],[194,221,]),'else':([169,194,],[195,209,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program_aux main','program',2,'p_program','parser.py',17),
  ('program -> main','program',1,'p_program','parser.py',18),
  ('program_aux -> program_aux function','program_aux',2,'p_program_aux','parser.py',22),
  ('program_aux -> function','program_aux',1,'p_program_aux','parser.py',23),
  ('function -> function_header function_body n_end_function','function',3,'p_function','parser.py',27),
  ('main -> FUNCTION MAIN n_start_main function_body n_end_function','main',5,'p_main','parser.py',31),
  ('function_header -> FUNCTION ID n_add_function_name L_PARENS function_params R_PARENS COLON function_type','function_header',8,'p_function_header','parser.py',35),
  ('function_header -> FUNCTION ID n_add_function_name L_PARENS R_PARENS COLON function_type','function_header',7,'p_function_header','parser.py',36),
  ('function_body -> L_KEY_BRACKET function_body_aux statements R_KEY_BRACKET','function_body',4,'p_function_body','parser.py',40),
  ('function_body -> L_KEY_BRACKET statements R_KEY_BRACKET','function_body',3,'p_function_body','parser.py',41),
  ('function_body_aux -> var function_body_aux','function_body_aux',2,'p_function_body_aux','parser.py',45),
  ('function_body_aux -> var','function_body_aux',1,'p_function_body_aux','parser.py',46),
  ('statements -> statement statements','statements',2,'p_statements','parser.py',50),
  ('statements -> statement','statements',1,'p_statements','parser.py',51),
  ('function_params -> type ID n_add_var array_index COMMA function_params','function_params',6,'p_function_params','parser.py',55),
  ('function_params -> type ID n_add_var array_index','function_params',4,'p_function_params','parser.py',56),
  ('function_params -> type ID n_add_var COMMA function_params','function_params',5,'p_function_params','parser.py',57),
  ('function_params -> type ID n_add_var','function_params',3,'p_function_params','parser.py',58),
  ('function_type -> INT n_add_function_type','function_type',2,'p_function_type','parser.py',62),
  ('function_type -> FLOAT n_add_function_type','function_type',2,'p_function_type','parser.py',63),
  ('function_type -> STRING n_add_function_type','function_type',2,'p_function_type','parser.py',64),
  ('function_type -> VOID n_add_function_type','function_type',2,'p_function_type','parser.py',65),
  ('var -> type_aux ID n_add_var array_dim var_aux SEMICOLON','var',6,'p_var','parser.py',69),
  ('var -> type_aux ID n_add_var array_dim SEMICOLON','var',5,'p_var','parser.py',70),
  ('var -> type_aux ID n_add_var var_aux SEMICOLON','var',5,'p_var','parser.py',71),
  ('var -> type_aux ID n_add_var SEMICOLON','var',4,'p_var','parser.py',72),
  ('type_aux -> GLOBAL type','type_aux',2,'p_type_aux','parser.py',76),
  ('type_aux -> type','type_aux',1,'p_type_aux','parser.py',77),
  ('var_aux -> COMMA ID n_add_var array_dim var_aux','var_aux',5,'p_var_aux','parser.py',81),
  ('var_aux -> COMMA ID n_add_var array_dim','var_aux',4,'p_var_aux','parser.py',82),
  ('var_aux -> COMMA ID n_add_var var_aux','var_aux',4,'p_var_aux','parser.py',83),
  ('var_aux -> COMMA ID n_add_var','var_aux',3,'p_var_aux','parser.py',84),
  ('statement -> statement_aux SEMICOLON','statement',2,'p_statement','parser.py',88),
  ('statement -> statement_aux_2','statement',1,'p_statement','parser.py',89),
  ('statement_aux -> assignment','statement_aux',1,'p_statement_aux','parser.py',93),
  ('statement_aux -> function_call','statement_aux',1,'p_statement_aux','parser.py',94),
  ('statement_aux -> return','statement_aux',1,'p_statement_aux','parser.py',95),
  ('statement_aux -> print','statement_aux',1,'p_statement_aux','parser.py',96),
  ('statement_aux_2 -> if','statement_aux_2',1,'p_statement_aux_2','parser.py',100),
  ('statement_aux_2 -> while','statement_aux_2',1,'p_statement_aux_2','parser.py',101),
  ('type -> INT n_record_last_type','type',2,'p_type','parser.py',105),
  ('type -> FLOAT n_record_last_type','type',2,'p_type','parser.py',106),
  ('type -> STRING n_record_last_type','type',2,'p_type','parser.py',107),
  ('array_index -> L_SQUARE_BRACKET expression R_SQUARE_BRACKET L_SQUARE_BRACKET expression R_SQUARE_BRACKET','array_index',6,'p_array_index','parser.py',111),
  ('array_index -> L_SQUARE_BRACKET expression R_SQUARE_BRACKET','array_index',3,'p_array_index','parser.py',112),
  ('array_dim -> L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET','array_dim',6,'p_array_dim','parser.py',116),
  ('array_dim -> L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET','array_dim',3,'p_array_dim','parser.py',117),
  ('assignment -> ID n_add_operand array_index ASSIGN n_make_assignment expression','assignment',6,'p_assignment','parser.py',121),
  ('assignment -> ID n_add_operand array_index ASSIGN n_make_assignment read','assignment',6,'p_assignment','parser.py',122),
  ('assignment -> ID n_add_operand ASSIGN n_make_assignment expression','assignment',5,'p_assignment','parser.py',123),
  ('assignment -> ID n_add_operand ASSIGN n_make_assignment read','assignment',5,'p_assignment','parser.py',124),
  ('function_call -> ID params_pass','function_call',2,'p_function_call','parser.py',128),
  ('return -> RETURN expression','return',2,'p_return','parser.py',132),
  ('if -> IF L_PARENS expression R_PARENS block elif else','if',7,'p_if','parser.py',136),
  ('if -> IF L_PARENS expression R_PARENS block elif','if',6,'p_if','parser.py',137),
  ('if -> IF L_PARENS expression R_PARENS block else','if',6,'p_if','parser.py',138),
  ('if -> IF L_PARENS expression R_PARENS block','if',5,'p_if','parser.py',139),
  ('elif -> ELIF L_PARENS expression R_PARENS block elif','elif',6,'p_elif','parser.py',143),
  ('elif -> ELIF L_PARENS expression R_PARENS block','elif',5,'p_elif','parser.py',144),
  ('else -> ELSE block','else',2,'p_else','parser.py',148),
  ('while -> WHILE L_PARENS expression R_PARENS block','while',5,'p_while','parser.py',152),
  ('print -> PRINT L_PARENS print_aux R_PARENS','print',4,'p_print','parser.py',156),
  ('print -> PRINT L_PARENS R_PARENS','print',3,'p_print','parser.py',157),
  ('print_aux -> CONST_STRING COMMA print_aux','print_aux',3,'p_print_aux','parser.py',161),
  ('print_aux -> CONST_STRING','print_aux',1,'p_print_aux','parser.py',162),
  ('print_aux -> ID COMMA print_aux','print_aux',3,'p_print_aux','parser.py',163),
  ('print_aux -> ID','print_aux',1,'p_print_aux','parser.py',164),
  ('expression -> exp n_eval_exp AND n_add_operator expression','expression',5,'p_expression','parser.py',168),
  ('expression -> exp n_eval_exp','expression',2,'p_expression','parser.py',169),
  ('read -> READ ID','read',2,'p_read','parser.py',173),
  ('params_pass -> L_PARENS expression params_pass_aux R_PARENS','params_pass',4,'p_params_pass','parser.py',177),
  ('params_pass -> L_PARENS expression R_PARENS','params_pass',3,'p_params_pass','parser.py',178),
  ('params_pass -> L_PARENS R_PARENS','params_pass',2,'p_params_pass','parser.py',179),
  ('params_pass_aux -> COMMA expression params_pass_aux','params_pass_aux',3,'p_params_pass_aux','parser.py',183),
  ('params_pass_aux -> COMMA expression','params_pass_aux',2,'p_params_pass_aux','parser.py',184),
  ('block -> L_KEY_BRACKET statements R_KEY_BRACKET','block',3,'p_block','parser.py',188),
  ('exp -> xp n_eval_xp OR n_add_operator exp','exp',5,'p_exp','parser.py',192),
  ('exp -> xp n_eval_xp','exp',2,'p_exp','parser.py',193),
  ('xp -> x n_eval_x log_op n_add_operator x','xp',5,'p_xp','parser.py',197),
  ('xp -> x n_eval_x','xp',2,'p_xp','parser.py',198),
  ('x -> term n_eval_term x_aux','x',3,'p_x','parser.py',202),
  ('x -> term n_eval_term','x',2,'p_x','parser.py',203),
  ('x_aux -> PLUS n_add_operator term x_aux','x_aux',4,'p_x_aux','parser.py',207),
  ('x_aux -> PLUS n_add_operator term','x_aux',3,'p_x_aux','parser.py',208),
  ('x_aux -> MINUS n_add_operator term x_aux','x_aux',4,'p_x_aux','parser.py',209),
  ('x_aux -> MINUS n_add_operator term','x_aux',3,'p_x_aux','parser.py',210),
  ('log_op -> NOT_EQUAL','log_op',1,'p_log_op','parser.py',214),
  ('log_op -> EQUALS','log_op',1,'p_log_op','parser.py',215),
  ('log_op -> GREATER','log_op',1,'p_log_op','parser.py',216),
  ('log_op -> GREATER_EQ','log_op',1,'p_log_op','parser.py',217),
  ('log_op -> LESS','log_op',1,'p_log_op','parser.py',218),
  ('log_op -> LESS_EQ','log_op',1,'p_log_op','parser.py',219),
  ('term -> factor n_eval_factor term_aux','term',3,'p_term','parser.py',223),
  ('term -> factor n_eval_factor','term',2,'p_term','parser.py',224),
  ('term_aux -> TIMES n_add_operator factor term_aux','term_aux',4,'p_term_aux','parser.py',228),
  ('term_aux -> TIMES n_add_operator factor','term_aux',3,'p_term_aux','parser.py',229),
  ('term_aux -> DIVIDE n_add_operator factor term_aux','term_aux',4,'p_term_aux','parser.py',230),
  ('term_aux -> DIVIDE n_add_operator factor','term_aux',3,'p_term_aux','parser.py',231),
  ('factor -> NOT factor_aux','factor',2,'p_factor','parser.py',235),
  ('factor -> factor_aux','factor',1,'p_factor','parser.py',236),
  ('factor_aux -> L_PARENS expression R_PARENS','factor_aux',3,'p_factor_aux','parser.py',240),
  ('factor_aux -> PLUS const','factor_aux',2,'p_factor_aux','parser.py',241),
  ('factor_aux -> MINUS const','factor_aux',2,'p_factor_aux','parser.py',242),
  ('factor_aux -> const','factor_aux',1,'p_factor_aux','parser.py',243),
  ('const -> ID n_add_operand','const',2,'p_const','parser.py',247),
  ('const -> CONST_I n_add_operand','const',2,'p_const','parser.py',248),
  ('const -> CONST_F n_add_operand','const',2,'p_const','parser.py',249),
  ('const -> CONST_STRING n_add_operand','const',2,'p_const','parser.py',250),
  ('const -> function_call','const',1,'p_const','parser.py',251),
  ('const -> array_access','const',1,'p_const','parser.py',252),
  ('array_access -> ID array_index','array_access',2,'p_array_access','parser.py',256),
  ('n_start_main -> <empty>','n_start_main',0,'p_n_start_main','parser.py',262),
  ('n_add_function_name -> <empty>','n_add_function_name',0,'p_n_add_function_name','parser.py',267),
  ('n_add_function_type -> <empty>','n_add_function_type',0,'p_n_add_function_type','parser.py',272),
  ('n_end_function -> <empty>','n_end_function',0,'p_n_end_function','parser.py',278),
  ('n_add_var -> <empty>','n_add_var',0,'p_n_add_var','parser.py',283),
  ('n_record_last_type -> <empty>','n_record_last_type',0,'p_n_record_last_type','parser.py',289),
  ('n_eval_exp -> <empty>','n_eval_exp',0,'p_n_eval_exp','parser.py',295),
  ('n_eval_xp -> <empty>','n_eval_xp',0,'p_n_eval_xp','parser.py',300),
  ('n_eval_x -> <empty>','n_eval_x',0,'p_n_eval_x','parser.py',305),
  ('n_eval_factor -> <empty>','n_eval_factor',0,'p_n_eval_factor','parser.py',310),
  ('n_eval_term -> <empty>','n_eval_term',0,'p_n_eval_term','parser.py',315),
  ('n_add_operand -> <empty>','n_add_operand',0,'p_n_add_operand','parser.py',320),
  ('n_add_operator -> <empty>','n_add_operator',0,'p_n_add_operator','parser.py',326),
  ('n_make_assignment -> <empty>','n_make_assignment',0,'p_n_make_assignment','parser.py',331),
]
