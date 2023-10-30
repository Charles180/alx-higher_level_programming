#include "lists.h"
/**
  *check_cycle - Fubcton to check if linked list has a cycle
  *
  *@list: The linked list to be checked
  *
  *Return: 1 if the list has a cycle else 0.
  */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
