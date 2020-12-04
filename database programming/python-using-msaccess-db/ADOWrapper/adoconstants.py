#
# Module: ADOConstants
# Author: Mayukh Bose
# Version: 0.0.1
# Purpose: To contain constant names for various ADO operations. Note that this is
#          not a comprehensive list of all constants.
# Modifications (push down list):
# 2004-February-15 - Released module to the public
#
# Copyright (c) 2004, Mayukh Bose
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:

#    Redistributions of source code must retain the above copyright notice, this list
# of conditions and the following disclaimer.
#    Redistributions in binary form must reproduce the above copyright notice, this
# list of conditions and the following disclaimer in the documentation and/or other
# materials provided with the distribution.
#    Neither the name of Mayukh Bose nor the names of other contributors may be used to
# endorse or promote products derived from this software without specific prior written
# permission.
#
#    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
    

#
# Data Type Constants
#

adEmpty                = 0
adSmallInt            = 2
adInteger            = 3
adSingle            = 4
adDouble            = 5
adCurrency            = 6
adDate                = 7
adBSTR                = 8
adIDispatch            = 9
adError                = 10
adBoolean            = 11
adVariant            = 12
adIUnknown            = 13
adDecimal            = 14
adTinyInt            = 16
adUnsignedTinyInt    = 17
adUnsignedSmallInt    = 18
adUnsignedInt       = 19
adBigInt            = 20
adUnsignedBigInt    = 21

adFileTime            = 64
adGUID                = 72

adBinary            = 128
adChar                = 129
adWChar                = 130
adNumeric            = 131
adUserDefined        = 132
adDBDate            = 133
adDBTime            = 134
adDBTimeStamp        = 135
adChapter            = 136
adDBFileTime        = 137
adPropVariant        = 138
adVarNumeric        = 139

adVarchar            = 200
adVarChar           = 200
adLongVarChar        = 201
adVarWChar            = 202
adLongVarWChar        = 203
adVarBinary            = 204
adLongVarBinary        = 205


#
# Connection State Constants
#
adStateClosed        = 0
adStateOpen            = 1
adStateConnecting    = 2
adStateExecuting    = 4
adStateFetching        = 8

#
# CursorType constants
#
adOpenUnspecified   = -1
adOpenForwardOnly   = 0
adOpenKeyset        = 1
adOpenDynamic       = 2
adOpenStatic        = 3

#
# LockType constants
#
adLockUnspecified   = -1
adLockReadOnly      = 1
adLockPessimistic   = 2
adLockOptimistic    = 3
adLockBatchOptimistic = 4

#
# ExecuteOption constants
#
adOptionUnspecified = -1
adAsyncExecute      = 16
adAsyncFetch        = 32
adAsyncFetchNonBlocking = 64
adExecuteNoRecords  = 128

#
# CursorLocation constants
#
adUseNone           = 1
adUseServer         = 2
adUseClient         = 3
adUseClientBatch    = 3

#
# ParameterDirection constants
#
adParamUnknown      = 0
adParamInput        = 1
adParamOutput       = 2
adParamInputOutput  = 3
adParamReturnValue  = 4

#
# ParameterAttributes constants
#
adParamSigned       = 16
adParamNullable     = 64
adParamLong         = 128

#
# CommandType constants
#
adCmdUnspecified    = -1
adCmdText           = 1
adCmdTable          = 2
adCmdStoredProc     = 4
adCmdUnknown        = 8
adCmdFile           = 256
adCmdTableDirect    = 512