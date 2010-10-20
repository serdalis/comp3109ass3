# $ANTLR 3.1.2 VPL.g 2010-10-21 01:49:29

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EXPONENT=21
RB=13
NUMBER=19
WHITESPACE=24
FLOAT=22
SEMICOLON=14
MIN=10
MINUS=7
MULT=8
EOF=-1
ALPHA=20
SCORE=17
COMMA=11
FUNC=4
EQUAL=15
IDENT=18
LB=12
PLUS=6
VAR=16
DIGIT=23
DIV=9
END=5


class VPLLexer(Lexer):

    grammarFileName = "VPL.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )

        self.dfa12 = self.DFA12(
            self, 12,
            eot = self.DFA12_eot,
            eof = self.DFA12_eof,
            min = self.DFA12_min,
            max = self.DFA12_max,
            accept = self.DFA12_accept,
            special = self.DFA12_special,
            transition = self.DFA12_transition
            )






    # $ANTLR start "FUNC"
    def mFUNC(self, ):

        try:
            _type = FUNC
            _channel = DEFAULT_CHANNEL

            # VPL.g:7:6: ( 'func' )
            # VPL.g:7:8: 'func'
            pass 
            self.match("func")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FUNC"



    # $ANTLR start "END"
    def mEND(self, ):

        try:
            _type = END
            _channel = DEFAULT_CHANNEL

            # VPL.g:8:5: ( 'end' )
            # VPL.g:8:7: 'end'
            pass 
            self.match("end")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "END"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # VPL.g:9:6: ( '+' )
            # VPL.g:9:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # VPL.g:10:7: ( '-' )
            # VPL.g:10:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "MULT"
    def mMULT(self, ):

        try:
            _type = MULT
            _channel = DEFAULT_CHANNEL

            # VPL.g:11:6: ( '*' )
            # VPL.g:11:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MULT"



    # $ANTLR start "DIV"
    def mDIV(self, ):

        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # VPL.g:12:5: ( '/' )
            # VPL.g:12:7: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIV"



    # $ANTLR start "MIN"
    def mMIN(self, ):

        try:
            _type = MIN
            _channel = DEFAULT_CHANNEL

            # VPL.g:13:5: ( 'min' )
            # VPL.g:13:7: 'min'
            pass 
            self.match("min")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MIN"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # VPL.g:14:7: ( ',' )
            # VPL.g:14:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "LB"
    def mLB(self, ):

        try:
            _type = LB
            _channel = DEFAULT_CHANNEL

            # VPL.g:15:4: ( '(' )
            # VPL.g:15:6: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LB"



    # $ANTLR start "RB"
    def mRB(self, ):

        try:
            _type = RB
            _channel = DEFAULT_CHANNEL

            # VPL.g:16:4: ( ')' )
            # VPL.g:16:6: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RB"



    # $ANTLR start "SEMICOLON"
    def mSEMICOLON(self, ):

        try:
            _type = SEMICOLON
            _channel = DEFAULT_CHANNEL

            # VPL.g:17:11: ( ';' )
            # VPL.g:17:13: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMICOLON"



    # $ANTLR start "EQUAL"
    def mEQUAL(self, ):

        try:
            _type = EQUAL
            _channel = DEFAULT_CHANNEL

            # VPL.g:18:7: ( '=' )
            # VPL.g:18:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUAL"



    # $ANTLR start "VAR"
    def mVAR(self, ):

        try:
            _type = VAR
            _channel = DEFAULT_CHANNEL

            # VPL.g:19:5: ( 'var' )
            # VPL.g:19:7: 'var'
            pass 
            self.match("var")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VAR"



    # $ANTLR start "SCORE"
    def mSCORE(self, ):

        try:
            _type = SCORE
            _channel = DEFAULT_CHANNEL

            # VPL.g:20:7: ( '_' )
            # VPL.g:20:9: '_'
            pass 
            self.match(95)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SCORE"



    # $ANTLR start "IDENT"
    def mIDENT(self, ):

        try:
            _type = IDENT
            _channel = DEFAULT_CHANNEL

            # VPL.g:56:7: ( ( ALPHA | SCORE )+ )
            # VPL.g:56:9: ( ALPHA | SCORE )+
            pass 
            # VPL.g:56:9: ( ALPHA | SCORE )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # VPL.g:
                    pass 
                    if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IDENT"



    # $ANTLR start "ALPHA"
    def mALPHA(self, ):

        try:
            # VPL.g:59:8: ( 'A' .. 'Z' | 'a' .. 'z' )
            # VPL.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ALPHA"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # VPL.g:62:5: ( ( NUMBER )+ '.' ( NUMBER )* ( EXPONENT )? | '.' ( NUMBER )+ EXPONENT | ( NUMBER )+ EXPONENT )
            alt7 = 3
            alt7 = self.dfa7.predict(self.input)
            if alt7 == 1:
                # VPL.g:62:9: ( NUMBER )+ '.' ( NUMBER )* ( EXPONENT )?
                pass 
                # VPL.g:62:9: ( NUMBER )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((48 <= LA2_0 <= 57)) :
                        alt2 = 1


                    if alt2 == 1:
                        # VPL.g:62:9: NUMBER
                        pass 
                        self.mNUMBER()


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                self.match(46)
                # VPL.g:62:21: ( NUMBER )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((48 <= LA3_0 <= 57)) :
                        alt3 = 1


                    if alt3 == 1:
                        # VPL.g:62:21: NUMBER
                        pass 
                        self.mNUMBER()


                    else:
                        break #loop3


                # VPL.g:62:29: ( EXPONENT )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 69 or LA4_0 == 101) :
                    alt4 = 1
                if alt4 == 1:
                    # VPL.g:62:29: EXPONENT
                    pass 
                    self.mEXPONENT()





            elif alt7 == 2:
                # VPL.g:63:9: '.' ( NUMBER )+ EXPONENT
                pass 
                self.match(46)
                # VPL.g:63:13: ( NUMBER )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((48 <= LA5_0 <= 57)) :
                        alt5 = 1


                    if alt5 == 1:
                        # VPL.g:63:13: NUMBER
                        pass 
                        self.mNUMBER()


                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1


                self.mEXPONENT()


            elif alt7 == 3:
                # VPL.g:64:9: ( NUMBER )+ EXPONENT
                pass 
                # VPL.g:64:9: ( NUMBER )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((48 <= LA6_0 <= 57)) :
                        alt6 = 1


                    if alt6 == 1:
                        # VPL.g:64:9: NUMBER
                        pass 
                        self.mNUMBER()


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                self.mEXPONENT()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):

        try:
            # VPL.g:68:11: ( ( 'e' | 'E' ) ( PLUS | MINUS )? ( NUMBER )+ )
            # VPL.g:68:13: ( 'e' | 'E' ) ( PLUS | MINUS )? ( NUMBER )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # VPL.g:68:23: ( PLUS | MINUS )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 43 or LA8_0 == 45) :
                alt8 = 1
            if alt8 == 1:
                # VPL.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # VPL.g:68:37: ( NUMBER )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((48 <= LA9_0 <= 57)) :
                    alt9 = 1


                if alt9 == 1:
                    # VPL.g:68:37: NUMBER
                    pass 
                    self.mNUMBER()


                else:
                    if cnt9 >= 1:
                        break #loop9

                    eee = EarlyExitException(9, self.input)
                    raise eee

                cnt9 += 1






        finally:

            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):

        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # VPL.g:70:8: ( ( DIGIT )+ )
            # VPL.g:70:10: ( DIGIT )+
            pass 
            # VPL.g:70:10: ( DIGIT )+
            cnt10 = 0
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((48 <= LA10_0 <= 57)) :
                    alt10 = 1


                if alt10 == 1:
                    # VPL.g:70:10: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt10 >= 1:
                        break #loop10

                    eee = EarlyExitException(10, self.input)
                    raise eee

                cnt10 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUMBER"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # VPL.g:73:8: ( '0' .. '9' )
            # VPL.g:73:10: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # VPL.g:75:12: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # VPL.g:75:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # VPL.g:75:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt11 = 0
            while True: #loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((9 <= LA11_0 <= 10) or (12 <= LA11_0 <= 13) or LA11_0 == 32) :
                    alt11 = 1


                if alt11 == 1:
                    # VPL.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt11 >= 1:
                        break #loop11

                    eee = EarlyExitException(11, self.input)
                    raise eee

                cnt11 += 1


            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    def mTokens(self):
        # VPL.g:1:8: ( FUNC | END | PLUS | MINUS | MULT | DIV | MIN | COMMA | LB | RB | SEMICOLON | EQUAL | VAR | SCORE | IDENT | FLOAT | NUMBER | WHITESPACE )
        alt12 = 18
        alt12 = self.dfa12.predict(self.input)
        if alt12 == 1:
            # VPL.g:1:10: FUNC
            pass 
            self.mFUNC()


        elif alt12 == 2:
            # VPL.g:1:15: END
            pass 
            self.mEND()


        elif alt12 == 3:
            # VPL.g:1:19: PLUS
            pass 
            self.mPLUS()


        elif alt12 == 4:
            # VPL.g:1:24: MINUS
            pass 
            self.mMINUS()


        elif alt12 == 5:
            # VPL.g:1:30: MULT
            pass 
            self.mMULT()


        elif alt12 == 6:
            # VPL.g:1:35: DIV
            pass 
            self.mDIV()


        elif alt12 == 7:
            # VPL.g:1:39: MIN
            pass 
            self.mMIN()


        elif alt12 == 8:
            # VPL.g:1:43: COMMA
            pass 
            self.mCOMMA()


        elif alt12 == 9:
            # VPL.g:1:49: LB
            pass 
            self.mLB()


        elif alt12 == 10:
            # VPL.g:1:52: RB
            pass 
            self.mRB()


        elif alt12 == 11:
            # VPL.g:1:55: SEMICOLON
            pass 
            self.mSEMICOLON()


        elif alt12 == 12:
            # VPL.g:1:65: EQUAL
            pass 
            self.mEQUAL()


        elif alt12 == 13:
            # VPL.g:1:71: VAR
            pass 
            self.mVAR()


        elif alt12 == 14:
            # VPL.g:1:75: SCORE
            pass 
            self.mSCORE()


        elif alt12 == 15:
            # VPL.g:1:81: IDENT
            pass 
            self.mIDENT()


        elif alt12 == 16:
            # VPL.g:1:87: FLOAT
            pass 
            self.mFLOAT()


        elif alt12 == 17:
            # VPL.g:1:93: NUMBER
            pass 
            self.mNUMBER()


        elif alt12 == 18:
            # VPL.g:1:100: WHITESPACE
            pass 
            self.mWHITESPACE()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\2\56\3\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\71\1\145\3\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\1"
        )

    DFA7_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\4\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    DFA7 = DFA
    # lookup tables for DFA #12

    DFA12_eot = DFA.unpack(
        u"\1\uffff\2\17\4\uffff\1\17\5\uffff\1\17\1\27\1\uffff\1\30\2\uffff"
        u"\4\17\2\uffff\1\17\1\36\1\37\1\40\1\41\4\uffff"
        )

    DFA12_eof = DFA.unpack(
        u"\42\uffff"
        )

    DFA12_min = DFA.unpack(
        u"\1\11\1\165\1\156\4\uffff\1\151\5\uffff\1\141\1\101\1\uffff\1\56"
        u"\2\uffff\1\156\1\144\1\156\1\162\2\uffff\1\143\4\101\4\uffff"
        )

    DFA12_max = DFA.unpack(
        u"\1\172\1\165\1\156\4\uffff\1\151\5\uffff\1\141\1\172\1\uffff\1"
        u"\145\2\uffff\1\156\1\144\1\156\1\162\2\uffff\1\143\4\172\4\uffff"
        )

    DFA12_accept = DFA.unpack(
        u"\3\uffff\1\3\1\4\1\5\1\6\1\uffff\1\10\1\11\1\12\1\13\1\14\2\uffff"
        u"\1\17\1\uffff\1\20\1\22\4\uffff\1\16\1\21\5\uffff\1\2\1\7\1\15"
        u"\1\1"
        )

    DFA12_special = DFA.unpack(
        u"\42\uffff"
        )

            
    DFA12_transition = [
        DFA.unpack(u"\2\22\1\uffff\2\22\22\uffff\1\22\7\uffff\1\11\1\12\1"
        u"\5\1\3\1\10\1\4\1\21\1\6\12\20\1\uffff\1\13\1\uffff\1\14\3\uffff"
        u"\32\17\4\uffff\1\16\1\uffff\4\17\1\2\1\1\6\17\1\7\10\17\1\15\4"
        u"\17"),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u"\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\21\1\uffff\12\20\13\uffff\1\21\37\uffff\1\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #12

    DFA12 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(VPLLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
