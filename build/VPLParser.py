# $ANTLR 3.1.2 VPL.g 2010-10-22 12:36:17

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EXPONENT=25
RB=17
NUMBER=23
WHITESPACE=28
FLOAT=26
SEMICOLON=18
MIN=14
MINUS=11
MULT=12
EOF=-1
DEFINES=6
ALPHA=24
SCORE=21
COMMA=15
FUNC=8
EQUAL=19
IDENT=22
STATEMENTS=7
BASE=4
PLUS=10
LB=16
VAR=20
DIGIT=27
DIV=13
END=9
PARAMS=5

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "BASE", "PARAMS", "DEFINES", "STATEMENTS", "FUNC", "END", "PLUS", "MINUS", 
    "MULT", "DIV", "MIN", "COMMA", "LB", "RB", "SEMICOLON", "EQUAL", "VAR", 
    "SCORE", "IDENT", "NUMBER", "ALPHA", "EXPONENT", "FLOAT", "DIGIT", "WHITESPACE"
]




class VPLParser(Parser):
    grammarFileName = "VPL.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)







                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "start"
    # VPL.g:35:1: start : ( function )* -> ^( BASE ( function )* ) ;
    def start(self, ):

        retval = self.start_return()
        retval.start = self.input.LT(1)

        root_0 = None

        function1 = None


        stream_function = RewriteRuleSubtreeStream(self._adaptor, "rule function")
        try:
            try:
                # VPL.g:35:7: ( ( function )* -> ^( BASE ( function )* ) )
                # VPL.g:35:9: ( function )*
                pass 
                # VPL.g:35:9: ( function )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == FUNC) :
                        alt1 = 1


                    if alt1 == 1:
                        # VPL.g:35:10: function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_start168)
                        function1 = self.function()

                        self._state.following.pop()
                        stream_function.add(function1.tree)


                    else:
                        break #loop1



                # AST Rewrite
                # elements: function
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 35:21: -> ^( BASE ( function )* )
                # VPL.g:35:24: ^( BASE ( function )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BASE, "BASE"), root_1)

                # VPL.g:35:31: ( function )*
                while stream_function.hasNext():
                    self._adaptor.addChild(root_1, stream_function.nextTree())


                stream_function.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "start"

    class function_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "function"
    # VPL.g:37:1: function : FUNC IDENT param define statements END ;
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FUNC2 = None
        IDENT3 = None
        END7 = None
        param4 = None

        define5 = None

        statements6 = None


        FUNC2_tree = None
        IDENT3_tree = None
        END7_tree = None

        try:
            try:
                # VPL.g:37:10: ( FUNC IDENT param define statements END )
                # VPL.g:37:12: FUNC IDENT param define statements END
                pass 
                root_0 = self._adaptor.nil()

                FUNC2=self.match(self.input, FUNC, self.FOLLOW_FUNC_in_function188)
                IDENT3=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_function191)

                IDENT3_tree = self._adaptor.createWithPayload(IDENT3)
                root_0 = self._adaptor.becomeRoot(IDENT3_tree, root_0)

                self._state.following.append(self.FOLLOW_param_in_function194)
                param4 = self.param()

                self._state.following.pop()
                self._adaptor.addChild(root_0, param4.tree)
                self._state.following.append(self.FOLLOW_define_in_function196)
                define5 = self.define()

                self._state.following.pop()
                self._adaptor.addChild(root_0, define5.tree)
                self._state.following.append(self.FOLLOW_statements_in_function198)
                statements6 = self.statements()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statements6.tree)
                END7=self.match(self.input, END, self.FOLLOW_END_in_function200)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "function"

    class param_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "param"
    # VPL.g:39:1: param : ( LB list RB )? -> ^( PARAMS list ) ;
    def param(self, ):

        retval = self.param_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB8 = None
        RB10 = None
        list9 = None


        LB8_tree = None
        RB10_tree = None
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_list = RewriteRuleSubtreeStream(self._adaptor, "rule list")
        try:
            try:
                # VPL.g:39:6: ( ( LB list RB )? -> ^( PARAMS list ) )
                # VPL.g:39:8: ( LB list RB )?
                pass 
                # VPL.g:39:8: ( LB list RB )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == LB) :
                    alt2 = 1
                if alt2 == 1:
                    # VPL.g:39:9: LB list RB
                    pass 
                    LB8=self.match(self.input, LB, self.FOLLOW_LB_in_param209) 
                    stream_LB.add(LB8)
                    self._state.following.append(self.FOLLOW_list_in_param211)
                    list9 = self.list()

                    self._state.following.pop()
                    stream_list.add(list9.tree)
                    RB10=self.match(self.input, RB, self.FOLLOW_RB_in_param213) 
                    stream_RB.add(RB10)




                # AST Rewrite
                # elements: list
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 39:22: -> ^( PARAMS list )
                # VPL.g:39:25: ^( PARAMS list )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMS, "PARAMS"), root_1)

                self._adaptor.addChild(root_1, stream_list.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "param"

    class list_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "list"
    # VPL.g:41:1: list : IDENT ( COMMA IDENT )* ;
    def list(self, ):

        retval = self.list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT11 = None
        COMMA12 = None
        IDENT13 = None

        IDENT11_tree = None
        COMMA12_tree = None
        IDENT13_tree = None

        try:
            try:
                # VPL.g:41:5: ( IDENT ( COMMA IDENT )* )
                # VPL.g:41:7: IDENT ( COMMA IDENT )*
                pass 
                root_0 = self._adaptor.nil()

                IDENT11=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_list230)

                IDENT11_tree = self._adaptor.createWithPayload(IDENT11)
                self._adaptor.addChild(root_0, IDENT11_tree)

                # VPL.g:41:13: ( COMMA IDENT )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == COMMA) :
                        alt3 = 1


                    if alt3 == 1:
                        # VPL.g:41:14: COMMA IDENT
                        pass 
                        COMMA12=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_list233)
                        IDENT13=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_list236)

                        IDENT13_tree = self._adaptor.createWithPayload(IDENT13)
                        self._adaptor.addChild(root_0, IDENT13_tree)



                    else:
                        break #loop3





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "list"

    class define_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "define"
    # VPL.g:43:1: define : ( VAR list SEMICOLON )? -> ^( DEFINES ( list )? ) ;
    def define(self, ):

        retval = self.define_return()
        retval.start = self.input.LT(1)

        root_0 = None

        VAR14 = None
        SEMICOLON16 = None
        list15 = None


        VAR14_tree = None
        SEMICOLON16_tree = None
        stream_VAR = RewriteRuleTokenStream(self._adaptor, "token VAR")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_list = RewriteRuleSubtreeStream(self._adaptor, "rule list")
        try:
            try:
                # VPL.g:43:7: ( ( VAR list SEMICOLON )? -> ^( DEFINES ( list )? ) )
                # VPL.g:43:9: ( VAR list SEMICOLON )?
                pass 
                # VPL.g:43:9: ( VAR list SEMICOLON )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == VAR) :
                    alt4 = 1
                if alt4 == 1:
                    # VPL.g:43:10: VAR list SEMICOLON
                    pass 
                    VAR14=self.match(self.input, VAR, self.FOLLOW_VAR_in_define247) 
                    stream_VAR.add(VAR14)
                    self._state.following.append(self.FOLLOW_list_in_define249)
                    list15 = self.list()

                    self._state.following.pop()
                    stream_list.add(list15.tree)
                    SEMICOLON16=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_define251) 
                    stream_SEMICOLON.add(SEMICOLON16)




                # AST Rewrite
                # elements: list
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 43:31: -> ^( DEFINES ( list )? )
                # VPL.g:43:34: ^( DEFINES ( list )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(DEFINES, "DEFINES"), root_1)

                # VPL.g:43:44: ( list )?
                if stream_list.hasNext():
                    self._adaptor.addChild(root_1, stream_list.nextTree())


                stream_list.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "define"

    class statements_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "statements"
    # VPL.g:45:1: statements : statement ( SEMICOLON statement )* -> ^( STATEMENTS ( statement )* ) ;
    def statements(self, ):

        retval = self.statements_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMICOLON18 = None
        statement17 = None

        statement19 = None


        SEMICOLON18_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # VPL.g:45:11: ( statement ( SEMICOLON statement )* -> ^( STATEMENTS ( statement )* ) )
                # VPL.g:45:13: statement ( SEMICOLON statement )*
                pass 
                self._state.following.append(self.FOLLOW_statement_in_statements269)
                statement17 = self.statement()

                self._state.following.pop()
                stream_statement.add(statement17.tree)
                # VPL.g:45:23: ( SEMICOLON statement )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == SEMICOLON) :
                        alt5 = 1


                    if alt5 == 1:
                        # VPL.g:45:24: SEMICOLON statement
                        pass 
                        SEMICOLON18=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_statements272) 
                        stream_SEMICOLON.add(SEMICOLON18)
                        self._state.following.append(self.FOLLOW_statement_in_statements274)
                        statement19 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement19.tree)


                    else:
                        break #loop5



                # AST Rewrite
                # elements: statement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 45:46: -> ^( STATEMENTS ( statement )* )
                # VPL.g:45:49: ^( STATEMENTS ( statement )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STATEMENTS, "STATEMENTS"), root_1)

                # VPL.g:45:62: ( statement )*
                while stream_statement.hasNext():
                    self._adaptor.addChild(root_1, stream_statement.nextTree())


                stream_statement.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "statements"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "statement"
    # VPL.g:47:1: statement : ( ( IDENT EQUAL e )? | IDENT LB list RB ) ;
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT20 = None
        EQUAL21 = None
        IDENT23 = None
        LB24 = None
        RB26 = None
        e22 = None

        list25 = None


        IDENT20_tree = None
        EQUAL21_tree = None
        IDENT23_tree = None
        LB24_tree = None
        RB26_tree = None

        try:
            try:
                # VPL.g:47:10: ( ( ( IDENT EQUAL e )? | IDENT LB list RB ) )
                # VPL.g:47:12: ( ( IDENT EQUAL e )? | IDENT LB list RB )
                pass 
                root_0 = self._adaptor.nil()

                # VPL.g:47:12: ( ( IDENT EQUAL e )? | IDENT LB list RB )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == IDENT) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == EQUAL) :
                        alt7 = 1
                    elif (LA7_1 == LB) :
                        alt7 = 2
                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae

                elif (LA7_0 == END or LA7_0 == SEMICOLON) :
                    alt7 = 1
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # VPL.g:47:13: ( IDENT EQUAL e )?
                    pass 
                    # VPL.g:47:13: ( IDENT EQUAL e )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == IDENT) :
                        alt6 = 1
                    if alt6 == 1:
                        # VPL.g:47:14: IDENT EQUAL e
                        pass 
                        IDENT20=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement295)

                        IDENT20_tree = self._adaptor.createWithPayload(IDENT20)
                        self._adaptor.addChild(root_0, IDENT20_tree)

                        EQUAL21=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_statement297)

                        EQUAL21_tree = self._adaptor.createWithPayload(EQUAL21)
                        root_0 = self._adaptor.becomeRoot(EQUAL21_tree, root_0)

                        self._state.following.append(self.FOLLOW_e_in_statement300)
                        e22 = self.e()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, e22.tree)





                elif alt7 == 2:
                    # VPL.g:47:33: IDENT LB list RB
                    pass 
                    IDENT23=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement306)

                    IDENT23_tree = self._adaptor.createWithPayload(IDENT23)
                    root_0 = self._adaptor.becomeRoot(IDENT23_tree, root_0)

                    LB24=self.match(self.input, LB, self.FOLLOW_LB_in_statement309)
                    self._state.following.append(self.FOLLOW_list_in_statement312)
                    list25 = self.list()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, list25.tree)
                    RB26=self.match(self.input, RB, self.FOLLOW_RB_in_statement314)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "statement"

    class e_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "e"
    # VPL.g:49:1: e : e2 ( ( PLUS | MINUS ) e2 )* ;
    def e(self, ):

        retval = self.e_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set28 = None
        e227 = None

        e229 = None


        set28_tree = None

        try:
            try:
                # VPL.g:49:2: ( e2 ( ( PLUS | MINUS ) e2 )* )
                # VPL.g:49:4: e2 ( ( PLUS | MINUS ) e2 )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_e2_in_e324)
                e227 = self.e2()

                self._state.following.pop()
                self._adaptor.addChild(root_0, e227.tree)
                # VPL.g:49:6: ( ( PLUS | MINUS ) e2 )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((PLUS <= LA8_0 <= MINUS)) :
                        alt8 = 1


                    if alt8 == 1:
                        # VPL.g:49:7: ( PLUS | MINUS ) e2
                        pass 
                        set28 = self.input.LT(1)
                        set28 = self.input.LT(1)
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set28), root_0)
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_e2_in_e333)
                        e229 = self.e2()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, e229.tree)


                    else:
                        break #loop8





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "e"

    class e2_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "e2"
    # VPL.g:51:1: e2 : e3 ( ( MULT | DIV ) e3 )* ;
    def e2(self, ):

        retval = self.e2_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set31 = None
        e330 = None

        e332 = None


        set31_tree = None

        try:
            try:
                # VPL.g:51:3: ( e3 ( ( MULT | DIV ) e3 )* )
                # VPL.g:51:5: e3 ( ( MULT | DIV ) e3 )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_e3_in_e2342)
                e330 = self.e3()

                self._state.following.pop()
                self._adaptor.addChild(root_0, e330.tree)
                # VPL.g:51:7: ( ( MULT | DIV ) e3 )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((MULT <= LA9_0 <= DIV)) :
                        alt9 = 1


                    if alt9 == 1:
                        # VPL.g:51:8: ( MULT | DIV ) e3
                        pass 
                        set31 = self.input.LT(1)
                        set31 = self.input.LT(1)
                        if (MULT <= self.input.LA(1) <= DIV):
                            self.input.consume()
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set31), root_0)
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_e3_in_e2351)
                        e332 = self.e3()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, e332.tree)


                    else:
                        break #loop9





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "e2"

    class min_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "min"
    # VPL.g:53:1: min : MIN LB e COMMA e RB ;
    def min(self, ):

        retval = self.min_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MIN33 = None
        LB34 = None
        COMMA36 = None
        RB38 = None
        e35 = None

        e37 = None


        MIN33_tree = None
        LB34_tree = None
        COMMA36_tree = None
        RB38_tree = None

        try:
            try:
                # VPL.g:53:5: ( MIN LB e COMMA e RB )
                # VPL.g:53:7: MIN LB e COMMA e RB
                pass 
                root_0 = self._adaptor.nil()

                MIN33=self.match(self.input, MIN, self.FOLLOW_MIN_in_min362)

                MIN33_tree = self._adaptor.createWithPayload(MIN33)
                root_0 = self._adaptor.becomeRoot(MIN33_tree, root_0)

                LB34=self.match(self.input, LB, self.FOLLOW_LB_in_min365)
                self._state.following.append(self.FOLLOW_e_in_min368)
                e35 = self.e()

                self._state.following.pop()
                self._adaptor.addChild(root_0, e35.tree)
                COMMA36=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_min370)
                self._state.following.append(self.FOLLOW_e_in_min373)
                e37 = self.e()

                self._state.following.pop()
                self._adaptor.addChild(root_0, e37.tree)
                RB38=self.match(self.input, RB, self.FOLLOW_RB_in_min375)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "min"

    class nest_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "nest"
    # VPL.g:55:1: nest : LB e RB ;
    def nest(self, ):

        retval = self.nest_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB39 = None
        RB41 = None
        e40 = None


        LB39_tree = None
        RB41_tree = None

        try:
            try:
                # VPL.g:55:6: ( LB e RB )
                # VPL.g:55:8: LB e RB
                pass 
                root_0 = self._adaptor.nil()

                LB39=self.match(self.input, LB, self.FOLLOW_LB_in_nest384)
                self._state.following.append(self.FOLLOW_e_in_nest387)
                e40 = self.e()

                self._state.following.pop()
                self._adaptor.addChild(root_0, e40.tree)
                RB41=self.match(self.input, RB, self.FOLLOW_RB_in_nest389)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "nest"

    class e3_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "e3"
    # VPL.g:57:1: e3 : ( IDENT | NUMBER | min | nest ) ;
    def e3(self, ):

        retval = self.e3_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT42 = None
        NUMBER43 = None
        min44 = None

        nest45 = None


        IDENT42_tree = None
        NUMBER43_tree = None

        try:
            try:
                # VPL.g:57:4: ( ( IDENT | NUMBER | min | nest ) )
                # VPL.g:57:6: ( IDENT | NUMBER | min | nest )
                pass 
                root_0 = self._adaptor.nil()

                # VPL.g:57:6: ( IDENT | NUMBER | min | nest )
                alt10 = 4
                LA10 = self.input.LA(1)
                if LA10 == IDENT:
                    alt10 = 1
                elif LA10 == NUMBER:
                    alt10 = 2
                elif LA10 == MIN:
                    alt10 = 3
                elif LA10 == LB:
                    alt10 = 4
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # VPL.g:57:7: IDENT
                    pass 
                    IDENT42=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_e3399)

                    IDENT42_tree = self._adaptor.createWithPayload(IDENT42)
                    self._adaptor.addChild(root_0, IDENT42_tree)



                elif alt10 == 2:
                    # VPL.g:57:15: NUMBER
                    pass 
                    NUMBER43=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_e3403)

                    NUMBER43_tree = self._adaptor.createWithPayload(NUMBER43)
                    self._adaptor.addChild(root_0, NUMBER43_tree)



                elif alt10 == 3:
                    # VPL.g:57:24: min
                    pass 
                    self._state.following.append(self.FOLLOW_min_in_e3407)
                    min44 = self.min()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, min44.tree)


                elif alt10 == 4:
                    # VPL.g:57:30: nest
                    pass 
                    self._state.following.append(self.FOLLOW_nest_in_e3411)
                    nest45 = self.nest()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, nest45.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "e3"


    # Delegated rules


 

    FOLLOW_function_in_start168 = frozenset([1, 8])
    FOLLOW_FUNC_in_function188 = frozenset([22])
    FOLLOW_IDENT_in_function191 = frozenset([16, 18, 20, 22])
    FOLLOW_param_in_function194 = frozenset([16, 18, 20, 22])
    FOLLOW_define_in_function196 = frozenset([16, 18, 20, 22])
    FOLLOW_statements_in_function198 = frozenset([9])
    FOLLOW_END_in_function200 = frozenset([1])
    FOLLOW_LB_in_param209 = frozenset([22])
    FOLLOW_list_in_param211 = frozenset([17])
    FOLLOW_RB_in_param213 = frozenset([1])
    FOLLOW_IDENT_in_list230 = frozenset([1, 15])
    FOLLOW_COMMA_in_list233 = frozenset([22])
    FOLLOW_IDENT_in_list236 = frozenset([1, 15])
    FOLLOW_VAR_in_define247 = frozenset([22])
    FOLLOW_list_in_define249 = frozenset([18])
    FOLLOW_SEMICOLON_in_define251 = frozenset([1])
    FOLLOW_statement_in_statements269 = frozenset([1, 18])
    FOLLOW_SEMICOLON_in_statements272 = frozenset([18, 22])
    FOLLOW_statement_in_statements274 = frozenset([1, 18])
    FOLLOW_IDENT_in_statement295 = frozenset([19])
    FOLLOW_EQUAL_in_statement297 = frozenset([14, 16, 22, 23])
    FOLLOW_e_in_statement300 = frozenset([1])
    FOLLOW_IDENT_in_statement306 = frozenset([16])
    FOLLOW_LB_in_statement309 = frozenset([22])
    FOLLOW_list_in_statement312 = frozenset([17])
    FOLLOW_RB_in_statement314 = frozenset([1])
    FOLLOW_e2_in_e324 = frozenset([1, 10, 11])
    FOLLOW_set_in_e326 = frozenset([14, 16, 22, 23])
    FOLLOW_e2_in_e333 = frozenset([1, 10, 11])
    FOLLOW_e3_in_e2342 = frozenset([1, 12, 13])
    FOLLOW_set_in_e2344 = frozenset([14, 16, 22, 23])
    FOLLOW_e3_in_e2351 = frozenset([1, 12, 13])
    FOLLOW_MIN_in_min362 = frozenset([16])
    FOLLOW_LB_in_min365 = frozenset([14, 16, 22, 23])
    FOLLOW_e_in_min368 = frozenset([15])
    FOLLOW_COMMA_in_min370 = frozenset([14, 16, 22, 23])
    FOLLOW_e_in_min373 = frozenset([17])
    FOLLOW_RB_in_min375 = frozenset([1])
    FOLLOW_LB_in_nest384 = frozenset([14, 16, 22, 23])
    FOLLOW_e_in_nest387 = frozenset([17])
    FOLLOW_RB_in_nest389 = frozenset([1])
    FOLLOW_IDENT_in_e3399 = frozenset([1])
    FOLLOW_NUMBER_in_e3403 = frozenset([1])
    FOLLOW_min_in_e3407 = frozenset([1])
    FOLLOW_nest_in_e3411 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("VPLLexer", VPLParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
