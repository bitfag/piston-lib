import re
from grapheneapi.graphenewsrpc import RPCError


def decodeRPCErrorMsg(e):
    """ Helper function to decode the raised Exception and give it a
        python Exception class
    """
    found = re.search(
        (
            "(10 assert_exception: Assert Exception\n|"
            "Assert Exception \(10\)\n|"
            "3030000 tx_missing_posting_auth)"
            ".*: (.*)\n"
        ),
        str(e),
        flags=re.M)
    if found:
        return found.group(2).strip()
    else:
        return str(e)


class NoAccessApi(RPCError):
    pass


class AlreadyTransactedThisBlock(RPCError):
    pass


class VoteWeightTooSmall(RPCError):
    pass


class OnlyVoteOnceEvery3Seconds(RPCError):
    pass


class AlreadyVotedSimilarily(RPCError):
    pass


class NoMethodWithName(RPCError):
    pass


class PostOnlyEvery5Min(RPCError):
    pass


class DuplicateTransaction(RPCError):
    pass


class MissingRequiredPostingAuthority(RPCError):
    pass


class UnhandledRPCError(RPCError):
    pass


class ExceededAllowedBandwidth(RPCError):
    pass

class InvalidAPICallFormat(Exception):
    """ This is an exception should be raised when calling a steemd instance without API
        API changed in golos 0.16.5 / 0.17.0
        See https://docs.google.com/document/d/1mauB7xVuyu8XtmzYKGGWaWC5hIdd9BCps0EqznLjepI/edit#
    """
    pass
