# Generated from .\grammar\Wang.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WangParser import WangParser
else:
    from WangParser import WangParser

# This class defines a complete generic visitor for a parse tree produced by WangParser.

class WangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WangParser#deduction.
    def visitDeduction(self, ctx:WangParser.DeductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#FormExpr.
    def visitFormExpr(self, ctx:WangParser.FormExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#sequence.
    def visitSequence(self, ctx:WangParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#SeqExpr.
    def visitSeqExpr(self, ctx:WangParser.SeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#AndExpr.
    def visitAndExpr(self, ctx:WangParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#Parens.
    def visitParens(self, ctx:WangParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#NotExpr.
    def visitNotExpr(self, ctx:WangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#Id.
    def visitId(self, ctx:WangParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#ImplyExpr.
    def visitImplyExpr(self, ctx:WangParser.ImplyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#OrExpr.
    def visitOrExpr(self, ctx:WangParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WangParser#BicondExpr.
    def visitBicondExpr(self, ctx:WangParser.BicondExprContext):
        return self.visitChildren(ctx)



del WangParser