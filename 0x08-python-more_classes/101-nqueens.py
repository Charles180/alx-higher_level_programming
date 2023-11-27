#!/usr/bin/python3
"""

The module resolves the N-Queen puzzle using backtracking

"""


def isSafe(m_queen, nqueen):
    """ Examine whether the queens can kill each other

    Args:
        m_queen: queen's position array
        nqueen: queen's num

    Returns:
        True: If queen can't kill each other
        False: queen can kill each other

    """

    for x in range(nqueen):

        if m_queen[x] == m_queen[nqueen]:
            return False

        if abs(m_queen[x] - m_queen[nqueen]) == abs(x - nqueen):
            return False

    return True


def print_result(m_queen, nqueen):
    """ Prints the list with the Queens positions

    Args:
        m_queen: Queen's positions array
        nqueen: queen's num

    """

    residual = []

    for x in range(nqueen):
        residual.append([x, m_queen[x]])

    print(residual)


def Queen(m_queen, nqueen):
    """ Recursive function for Backtracking

    Args:
        m_queen: queen's position array
        nqueen: queen's num

    """

    if nqueen is len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1

    while((m_queen[nqueen] < len(m_queen) - 1)):

        m_queen[nqueen] += 1

        if isSafe(m_queen, nqueen) is True:

            if nqueen is not len(m_queen):
                Queen(m_queen, nqueen + 1)


def solveNQueen(size):
    """ Executes Backtracking

    Args:
        size: chessboard size

    """

    m_queen = [-1 for x in range(size)]

    Queen(m_queen, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a num")
        sys.exit(1)

    if size < 4:
        print("N must be >= 4")
        sys.exit(1)

    solveNQueen(size)
