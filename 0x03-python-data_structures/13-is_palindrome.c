#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *prev, *next, *tmp;

	if (!head || !*head || !(*head)->next)
		return (1);
	fast = *head;
	slow = *head;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	prev = NULL;
	tmp = slow;
	while (tmp)
	{
		next = tmp->next;
		tmp->next = prev;
		prev = tmp;
		tmp = next;
	}
	fast = *head;
	while (prev)
	{
		if (fast->n != prev->n)
			return (0);
		fast = fast->next;
		prev = prev->next;
	}
	return (1);
}
