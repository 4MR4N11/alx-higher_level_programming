#include "lists.h"

/**
 * reverse_list - reverses a listint_t linked list
 * @head: pointer to head of list
 * Return: pointer to first node of reversed list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *copy_head = NULL, *tmp = *head;

	if (!head || !*head)
		return (1);
	while (tmp)
	{
		add_nodeint_end(&copy_head, tmp->n);
		tmp = tmp->next;
	}
	tmp = *head;
	copy_head = reverse_list(copy_head);
	while (tmp && copy_head)
	{
		if (tmp->n != copy_head->n)
			return (0);
		tmp = tmp->next;
		copy_head = copy_head->next;
	}
	free_listint(copy_head);
	return (1);
}
