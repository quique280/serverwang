# Generated from .\grammar\Wang.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\2\3\2\3\3\3\3\3\3\5\3\32")
        buf.write("\n\3\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\5\4$\n\4\3\5\3\5")
        buf.write("\3\5\7\5)\n\5\f\5\16\5,\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6\66\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\7\6D\n\6\f\6\16\6G\13\6\3\6\2\3\n\7\2\4\6")
        buf.write("\b\n\2\2\2O\2\f\3\2\2\2\4 \3\2\2\2\6#\3\2\2\2\b%\3\2\2")
        buf.write("\2\n\65\3\2\2\2\f\21\5\4\3\2\r\16\7\6\2\2\16\20\5\4\3")
        buf.write("\2\17\r\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2")
        buf.write("\2\2\22\24\3\2\2\2\23\21\3\2\2\2\24\25\7\2\2\3\25\3\3")
        buf.write("\2\2\2\26\31\5\6\4\2\27\30\7\7\2\2\30\32\5\6\4\2\31\27")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32!\3\2\2\2\33\34\5\6\4\2\34\35")
        buf.write("\7\7\2\2\35!\3\2\2\2\36\37\7\7\2\2\37!\5\6\4\2 \26\3\2")
        buf.write("\2\2 \33\3\2\2\2 \36\3\2\2\2!\5\3\2\2\2\"$\5\b\5\2#\"")
        buf.write("\3\2\2\2#$\3\2\2\2$\7\3\2\2\2%*\5\n\6\2&\'\7\5\2\2\')")
        buf.write("\5\n\6\2(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\t\3")
        buf.write("\2\2\2,*\3\2\2\2-.\b\6\1\2./\7\b\2\2/\66\5\n\6\t\60\66")
        buf.write("\7\r\2\2\61\62\7\3\2\2\62\63\5\n\6\2\63\64\7\4\2\2\64")
        buf.write("\66\3\2\2\2\65-\3\2\2\2\65\60\3\2\2\2\65\61\3\2\2\2\66")
        buf.write("E\3\2\2\2\678\f\b\2\289\7\t\2\29D\5\n\6\t:;\f\7\2\2;<")
        buf.write("\7\n\2\2<D\5\n\6\b=>\f\6\2\2>?\7\13\2\2?D\5\n\6\6@A\f")
        buf.write("\5\2\2AB\7\f\2\2BD\5\n\6\6C\67\3\2\2\2C:\3\2\2\2C=\3\2")
        buf.write("\2\2C@\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\13\3\2\2")
        buf.write("\2GE\3\2\2\2\n\21\31 #*\65CE")
        return buf.getvalue()


class WangParser ( Parser ):

    grammarFileName = "Wang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'.'", "'=>'", "'~'", 
                     "'&'", "'|'", "'->'", "'<=>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "COMMA", "DOT", 
                      "LEADSTO", "NOT", "AND", "OR", "IMPLIES", "BICONDITIONAL", 
                      "ID", "WS", "ErrorChar" ]

    RULE_deduction = 0
    RULE_formula = 1
    RULE_sequence = 2
    RULE_listexpr = 3
    RULE_expr = 4

    ruleNames =  [ "deduction", "formula", "sequence", "listexpr", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    COMMA=3
    DOT=4
    LEADSTO=5
    NOT=6
    AND=7
    OR=8
    IMPLIES=9
    BICONDITIONAL=10
    ID=11
    WS=12
    ErrorChar=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class DeductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.FormulaContext)
            else:
                return self.getTypedRuleContext(WangParser.FormulaContext,i)


        def EOF(self):
            return self.getToken(WangParser.EOF, 0)

        def getRuleIndex(self):
            return WangParser.RULE_deduction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeduction" ):
                return visitor.visitDeduction(self)
            else:
                return visitor.visitChildren(self)




    def deduction(self):

        localctx = WangParser.DeductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_deduction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.formula()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==WangParser.DOT:
                self.state = 11
                self.match(WangParser.DOT)
                self.state = 12
                self.formula()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(WangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WangParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FormExprContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.SequenceContext)
            else:
                return self.getTypedRuleContext(WangParser.SequenceContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormExpr" ):
                return visitor.visitFormExpr(self)
            else:
                return visitor.visitChildren(self)



    def formula(self):

        localctx = WangParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = WangParser.FormExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.sequence()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==WangParser.LEADSTO:
                    self.state = 21
                    self.match(WangParser.LEADSTO)
                    self.state = 22
                    self.sequence()


                pass

            elif la_ == 2:
                localctx = WangParser.FormExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.sequence()
                self.state = 26
                self.match(WangParser.LEADSTO)
                pass

            elif la_ == 3:
                localctx = WangParser.FormExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(WangParser.LEADSTO)
                self.state = 29
                self.sequence()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listexpr(self):
            return self.getTypedRuleContext(WangParser.ListexprContext,0)


        def getRuleIndex(self):
            return WangParser.RULE_sequence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = WangParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << WangParser.T__0) | (1 << WangParser.NOT) | (1 << WangParser.ID))) != 0):
                self.state = 32
                self.listexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WangParser.RULE_listexpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SeqExprContext(ListexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ListexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeqExpr" ):
                return visitor.visitSeqExpr(self)
            else:
                return visitor.visitChildren(self)



    def listexpr(self):

        localctx = WangParser.ListexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listexpr)
        self._la = 0 # Token type
        try:
            localctx = WangParser.SeqExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.expr(0)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==WangParser.COMMA:
                self.state = 36
                self.match(WangParser.COMMA)
                self.state = 37
                self.expr(0)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ImplyExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplyExpr" ):
                return visitor.visitImplyExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class BicondExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBicondExpr" ):
                return visitor.visitBicondExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WangParser.NOT]:
                localctx = WangParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                self.match(WangParser.NOT)
                self.state = 45
                self.expr(7)
                pass
            elif token in [WangParser.ID]:
                localctx = WangParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(WangParser.ID)
                pass
            elif token in [WangParser.T__0]:
                localctx = WangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(WangParser.T__0)
                self.state = 48
                self.expr(0)
                self.state = 49
                self.match(WangParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 65
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = WangParser.AndExprContext(self, WangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 54
                        localctx.op = self.match(WangParser.AND)
                        self.state = 55
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = WangParser.OrExprContext(self, WangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 57
                        localctx.op = self.match(WangParser.OR)
                        self.state = 58
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = WangParser.ImplyExprContext(self, WangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 60
                        localctx.op = self.match(WangParser.IMPLIES)
                        self.state = 61
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = WangParser.BicondExprContext(self, WangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 63
                        localctx.op = self.match(WangParser.BICONDITIONAL)
                        self.state = 64
                        self.expr(4)
                        pass

             
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




