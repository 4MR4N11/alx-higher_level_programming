#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int stack[1000], top = -1;

	if (!head || !*head || !(*head)->next)
		return (1);
	tmp = *head;
	while (tmp)
	{
		stack[++top] = tmp->n;
		tmp = tmp->next;
	}
	tmp = *head;
	while (tmp)
	{
		if (tmp->n != stack[top--])
			return (0);
		tmp = tmp->next;
	}
	return (1);
}
