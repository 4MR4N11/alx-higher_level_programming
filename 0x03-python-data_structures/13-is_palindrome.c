#include "lists.h"

/**
 * get_list_len - get the length of a linked list
 * @h: pointer to head of list
 * Return: length of list
 */

int get_list_len(listint_t *h)
{
	int size;

	size = 0;
	while (h)
	{
		size++;
		h = h->next;
	}
	return (size);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int *half_list;
	listint_t *tmp;
	int half_len, list_len, i = 0;

	if (!head)
		return (1);
	tmp = *head;
	list_len = get_list_len(tmp);
	half_len = get_list_len(tmp) / 2;
	half_list = malloc(sizeof(int) * half_len);
	if (!half_list)
		return (0);
	while (tmp && i < half_len)
	{
		half_list[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	if (list_len % 2 != 0)
		tmp = tmp->next;
	i = half_len - 1;
	while (tmp && i >= 0)
	{
		if (tmp->n != half_list[i])
		{
			free(half_list);
			return (0);
		}
		i--;
		tmp = tmp->next;
	}
	free(half_list);
	return (1);
}
