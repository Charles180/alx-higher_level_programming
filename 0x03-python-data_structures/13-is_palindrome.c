#include "lists.h"
#include <stddef.h>
/**
  *reverse_listint - The function that reverses a linked list
  *
  *@head: The pointer to head of list.
  *
  *Return: pointer
  */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *updated = *head;
	listint_t *next = NULL;

	while (updated)
	{
		next = updated->next;
		updated->next = previous;
		previous = updated;
		updated = next;
	}
	*head = previous;
}
/**
  *is_palindrome - The function checks if a linked list is a palindrome
  *
  *@head: A double pointer to the linked list
  *
  *Return: 1 if palindrome, else 0
  */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *tmp = *head, *duplicate = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			duplicate = slow->next;
			break;
		}
		if (!fast->next)
		{
			duplicate = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_listint(&duplicate);
	while (duplicate && tmp)
	{
		if (tmp->n == duplicate->n)
		{
			duplicate = duplicate->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}
	if (!duplicate)
		return (1);
	return (0);
}
